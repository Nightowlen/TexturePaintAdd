# imports
import bpy
from bpy.types import Operator
from bpy.props import *
from . import Panel


class NPRSetRes(Operator):
    bl_idname = 'shading.set_res_img'
    bl_label = "Set this resolution"
    bl_description = "Set image resolution of this property"
    bl_options = {'REGISTER', "UNDO"}
    cpropimage: bpy.props.StringProperty()
    imageres: bpy.props.IntProperty()

    def set_resolution(self):

        image = bpy.context.scene
        cpropimage = self.cpropimage
        imageres = self.imageres

        textures = ['alpha', 'prefix', 'tex1', 'tex2', 'tex3']

        for textures in textures:
            if cpropimage == "alpha":
                image.set_res_width_alpha = imageres
                image.set_res_height_alpha = imageres
            elif cpropimage == "prefix":
                image.set_res_width_prefix = imageres
                image.set_res_height_prefix = imageres
            elif cpropimage == "tex1":
                image.set_res_width_tex1 = imageres
                image.set_res_height_tex1 = imageres
            elif cpropimage == "tex2":
                image.set_res_width_tex2 = imageres
                image.set_res_height_tex2 = imageres
            elif cpropimage == "tex3":
                image.set_res_width_tex3 = imageres
                image.set_res_height_tex3 = imageres

    def execute(self, context):

        self.set_resolution()

        return {'FINISHED'}


# Alpha add image
class NPRAddImg1(Operator):
    bl_idname = 'shading.add_img'
    bl_label = "Add image"
    bl_description = "Add an alpha paint image to selected object"
    bl_options = {'REGISTER', "UNDO"}

    # Generate a blank image with alpha channel
    def create_alpha_img(self, node_tree):
        cs = bpy.context.scene
        width = cs.set_res_width_alpha
        height = cs.set_res_height_alpha
        color = cs.set_alpha_color

        material = bpy.context.object.active_material

        node_tree = material.node_tree
        img_name_alpha_paint = bpy.context.selected_objects[0].name_full + "_" + "alpha" + "_" + "paint"

        img_node = node_tree.nodes.new('ShaderNodeTexImage')
        img_name = img_name_alpha_paint
        img_width = width
        img_height = height

        image = bpy.data.images.new(img_name, width=img_width, height=img_height)
        image.colorspace_settings.name = "sRGB"
        image.generated_color = color

        img_node.image = image
        return img_node

    # Generate MixRGB node
    def create_mix_rgb(self, node_tree):
        return node_tree.nodes.new('ShaderNodeMixRGB')  # ShaderNodeMixRGB

    # Connect Alpha img and MixRGB node
    def add_link(self, node_tree, node, node2, output_name, input_name, output_name2, input_name2):
        node_tree.links.new(node.outputs[output_name], node2.inputs[input_name])
        node_tree.links.new(node.outputs[output_name2], node2.inputs[input_name2])

        # Set location
        node.location = -500, 0
        node2.location = -200, 0

    # Add alpha image with image node and mix node to selected objects material        
    def execute(self, context):
        material = bpy.context.object.active_material
        node_tree = material.node_tree

        obj = bpy.context.selected_objects

        # Check if object is selected, probably better to just use active material since you can select other things
        # while the node tree is open. But this way there is no confusion about where the nodes will end up.
        if obj == []:  # "[]" is just the empty list
            self.report({'ERROR'}, "No active mesh object to add nodes.")
            return {'CANCELLED'}

        else:
            # Create Image and MixRGB
            create_alpha_img = self.create_alpha_img(node_tree)
            create_mix_rgb = self.create_mix_rgb(node_tree)
            # Connect nodes to inputs and outputs
            self.add_link(node_tree, create_alpha_img, create_mix_rgb, "Alpha", "Fac", "Color", "Color2")

        return {'FINISHED'}


class NPRAddImg2(Operator):
    bl_idname = 'shading.add_img_npr'
    bl_label = "Add image"
    bl_description = "Add images to selected object"
    bl_options = {'REGISTER', "UNDO"}

    def create_npr_nodes(self):
        cs = bpy.context.scene
        obj = bpy.context.selected_objects
        texturesname = ['prefix', 'tex1', 'tex2', 'tex3']

        # Check if object is selected, probably better to just use active material since you can select other things
        # while the node tree is open. But this way there is no confusion about where the nodes will end up.
        if obj == []:  # "[]" is just the empty list
            self.report({'ERROR'}, "No active mesh object to add nodes.")
            return {'CANCELLED'}
        else:
            material = bpy.context.object.active_material

        # material = bpy.context.object.active_material

        node_tree = material.node_tree

        # Make mixRGB nodes
        mix_rgb1 = node_tree.nodes.new('ShaderNodeMixRGB')
        mix_rgb1.blend_type = 'SCREEN'
        mix_rgb1.inputs[0].default_value = 1

        mix_rgb2 = node_tree.nodes.new('ShaderNodeMixRGB')
        mix_rgb2.blend_type = 'MULTIPLY'
        mix_rgb2.inputs[0].default_value = 1

        mix_rgb3 = node_tree.nodes.new('ShaderNodeMixRGB')
        mix_rgb3.blend_type = 'MULTIPLY'
        mix_rgb3.inputs[0].default_value = 1

        for texture in texturesname:

            name = getattr(cs, "set_" + texture + "_name")
            # Set prefix name before the names of the others
            if texture != "prefix":
                name = getattr(cs, "set_prefix_name") + "_" + name
            else:
                name = cs.set_prefix_name

            nodename = texture

            width = getattr(cs, "set_res_width_" + texture)
            height = getattr(cs, "set_res_height_" + texture)
            color = getattr(cs, "set_" + texture + "_color")

            image = bpy.data.images.new(name, width, height)
            image.colorspace_settings.name = "sRGB"
            # image.generated_color = (0, 0, 0, 0)
            image.generated_color = color

            material = bpy.context.object.active_material
            node_tree = material.node_tree

            texture = node_tree.nodes.new('ShaderNodeTexImage')

            texture.image = image
            image

            output_name = "Color"
            input_name = "Color1"
            input_name2 = "Color2"

            link = node_tree.links

            # link images and mixRGB
            if nodename == "prefix":
                # prefix img and light
                link.new(texture.outputs[output_name], mix_rgb1.inputs[input_name])
                texture.location = -1000, 0
                mix_rgb1.location = -700, -50
            if nodename == "tex1":
                # light img and shadow
                link.new(texture.outputs[output_name], mix_rgb1.inputs[input_name2])
                link.new(mix_rgb1.outputs[output_name], mix_rgb2.inputs[input_name])
                texture.location = -1000, -300
                mix_rgb2.location = -400, -150
            if nodename == "tex2":
                # shadow and shadow2
                link.new(texture.outputs[output_name], mix_rgb2.inputs[input_name2])
                link.new(mix_rgb2.outputs[output_name], mix_rgb3.inputs[input_name])
                texture.location = -700, -400
                mix_rgb3.location = -120, -250
            if nodename == "tex3":
                link.new(texture.outputs[output_name], mix_rgb3.inputs[input_name2])
                texture.location = -400, -500

    def execute(self, context):
        # Add npr images with image nodes and MixRGB nodes to selected objects material
        self.create_npr_nodes()

        return {'FINISHED'}
