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

        img_512 = 512
        img_1k = 1024
        img_2k = 2048
        img_4k = 4096

        # Prefix
        row = layout.row()

        split = row.split(align=True)
        col = split.column()
        col.label(text="Prefix Texture")

        split = row.split(align=True)
        col = split.column()
        col.prop(context.scene, "set_prefix_color", text="")

        split = row.split(align=True)
        col = split.column()
        col.prop(context.scene, "set_prefix_name", text="Name")

        # Prefix manual sizes
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Resolution")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_width_prefix", text="Width")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_height_prefix", text="Height")

        row = layout.row()

        props = row.operator('shading.set_res_img', text="Image Size 512")
        props.cpropimage = 'prefix'
        props.imageres = img_512

        props = row.operator('shading.set_res_img', text="Image Size 1K")
        props.cpropimage = 'prefix'
        props.imageres = img_1k

        props = row.operator('shading.set_res_img', text="Image Size 2K")
        props.cpropimage = 'prefix'
        props.imageres = img_2k

        props = row.operator('shading.set_res_img', text="Image Size 4K")
        props.cpropimage = 'prefix'
        props.imageres = img_4k

        layout.separator()

        # light
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Texture 1")

        split = row.split(align=True)
        col = split.column()
        col.prop(context.scene, "set_tex1_color", text="")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_tex1_name", text="Name")

        # light manual sizes
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Resolution")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_width_tex1", text="Width")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_height_tex1", text="Height")

        row = layout.row()

        props = row.operator('shading.set_res_img', text="Image Size 512")
        props.cpropimage = 'tex1'
        props.imageres = img_512

        props = row.operator('shading.set_res_img', text="Image Size 1K")
        props.cpropimage = 'tex1'
        props.imageres = img_1k

        props = row.operator('shading.set_res_img', text="Image Size 2K")
        props.cpropimage = 'tex1'
        props.imageres = img_2k

        props = row.operator('shading.set_res_img', text="Image Size 4K")
        props.cpropimage = 'tex1'
        props.imageres = img_4k

        layout.separator()

        # shadow
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Texture 2")

        split = row.split(align=True)
        col = split.column()
        col.prop(context.scene, "set_tex2_color", text="")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_tex2_name", text="Name")

        # shadow manual sizes
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Resolution")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_width_tex2", text="Width")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_height_tex2", text="Height")

        row = layout.row()

        props = row.operator('shading.set_res_img', text="Image Size 512")
        props.cpropimage = 'tex2'
        props.imageres = img_512

        props = row.operator('shading.set_res_img', text="Image Size 1K")
        props.cpropimage = 'tex2'
        props.imageres = img_1k

        props = row.operator('shading.set_res_img', text="Image Size 2K")
        props.cpropimage = 'tex2'
        props.imageres = img_2k

        props = row.operator('shading.set_res_img', text="Image Size 4K")
        props.cpropimage = 'tex2'
        props.imageres = img_4k

        layout.separator()

        # shadow 2
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Texture 3")

        split = row.split(align=True)
        col = split.column()
        col.prop(context.scene, "set_tex3_color", text="")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_tex3_name", text="Name")

        # shadow 2 manual sizes
        row = layout.row()

        split = row.split(factor=1, align=True)
        col = split.column()
        col.label(text="Resolution")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_width_tex3", text="Width")

        split = row.split(factor=1, align=True)
        col = split.column()
        col.prop(context.scene, "set_res_height_tex3", text="Height")

        row = layout.row()

        props = row.operator('shading.set_res_img', text="Image Size 512")
        props.cpropimage = 'tex3'
        props.imageres = img_512

        props = row.operator('shading.set_res_img', text="Image Size 1K")
        props.cpropimage = 'tex3'
        props.imageres = img_1k

        props = row.operator('shading.set_res_img', text="Image Size 2K")
        props.cpropimage = 'tex3'
        props.imageres = img_2k

        props = row.operator('shading.set_res_img', text="Image Size 4K")
        props.cpropimage = 'tex3'
        props.imageres = img_4k

        # Add images
        layout.separator()
        row = layout.row()
        row.operator('shading.add_img_npr', text="Add Images", icon='ADD')
