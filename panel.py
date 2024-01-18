import bpy
from bpy.types import Panel
from bpy.types import Operator
from bpy.props import *


class NPRPanel(Panel):
    bl_idname = "OBJECT_PT_TexturePaintAdd"
    bl_category = "TexturePaintAdd"
    bl_label = "Add Alpha paint Image Texture"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        img_512 = 512
        img_1k = 1024
        img_2k = 2048
        img_4k = 4096

        # Alpha image

        # manual sizes
        row = layout.row()
        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Resolution")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_width_alpha", text="Width")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_height_alpha", text="Height")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_alpha_color", text='')

        # add size click buttons
        row = layout.row()

        props = row.operator('shading.set_res_img', text="Image Size 512")
        props.cpropimage = 'alpha'
        props.imageres = img_512

        props = row.operator('shading.set_res_img', text="Image Size 1K")
        props.cpropimage = 'alpha'
        props.imageres = img_1k

        props = row.operator('shading.set_res_img', text="Image Size 2K")
        props.cpropimage = 'alpha'
        props.imageres = img_2k

        props = row.operator('shading.set_res_img', text="Image Size 4K")
        props.cpropimage = 'alpha'
        props.imageres = img_4k

        layout.separator()
        # Add img
        row = layout.row()
        row.operator('shading.add_img', text="Add Image", icon='ADD')


class NPRPanel2(Panel):
    bl_idname = "object_PT_TexturePaintAdd2"
    bl_category = "TexturePaintAdd"
    bl_label = "Add NPR Image Textures"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        img_sizes = [512, 1024, 2048, 4096]
        img_sizes_name = ["512", "1K", "2K", "4K"]

        def draw_texture_row(label, color_prop, name_prop, width_prop, height_prop, cpropimage):
            
            # Texture 
            row = layout.row()
            split = row.split(factor=1, align=True)
            col = split.column()
            col.label(text=label)

            split = row.split(align=True)
            col = split.column()
            col.prop(context.scene, color_prop, text="")

            split = row.split(factor=1, align=True)
            col = split.column()
            col.prop(context.scene, name_prop, text="Name")

            # Texture manual sizes
            row = layout.row()
            split = row.split(factor=1, align=True)
            col = split.column()
            col.label(text="Resolution")

            split = row.split(factor=1, align=True)
            col = split.column()
            col.prop(context.scene, width_prop, text="Width")

            split = row.split(factor=1, align=True)
            col = split.column()
            col.prop(context.scene, height_prop, text="Height")

            row = layout.row()
            for size, size_name in zip(img_sizes, img_sizes_name):
                props = row.operator('shading.set_res_img', text=f"Image Size {size_name}")
                props.cpropimage = cpropimage
                props.imageres = size

            layout.separator()

        draw_texture_row("Prefix Texture", "set_prefix_color", "set_prefix_name", "set_res_width_prefix", "set_res_height_prefix", 'prefix')
        draw_texture_row("Texture 1", "set_tex1_color", "set_tex1_name", "set_res_width_tex1", "set_res_height_tex1", 'tex1')
        draw_texture_row("Texture 2", "set_tex2_color", "set_tex2_name", "set_res_width_tex2", "set_res_height_tex2", 'tex2')
        draw_texture_row("Texture 3", "set_tex3_color", "set_tex3_name", "set_res_width_tex3", "set_res_height_tex3", 'tex3')

        # Add images
        layout.separator()
        row = layout.row()
        row.operator('shading.add_img_npr', text="Add Images", icon='ADD')