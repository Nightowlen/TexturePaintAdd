bl_info = {
    "name": "TexturePaintAdd",
    "author": "",
    "description": "Blender Addon to add image textures nodes to objects for a faster workflow",
    "blender": (3, 2, 0),
    "version": (0, 3, 0),
    "location": "Node Editor > Properties",
    "category": "Node"
}

# imports
import bpy
from bpy.props import *
from .panel import *
from .operators import *

# textures Alpha properties
# bpy.types.Scene.Select_res_alpha = PointerProperty(type=bpy.types.Object)
bpy.types.Scene.set_res_width_alpha = bpy.props.IntProperty(name="Image Width", description="Width of image",
                                                            default=2048)
bpy.types.Scene.set_res_height_alpha = bpy.props.IntProperty(name="Image Height", description="Height of image",
                                                             default=2048)
bpy.types.Scene.set_alpha_color = bpy.props.FloatVectorProperty(name="Alpha Color",
                                                                description="Color of generated image", size=4, min=0.0,
                                                                max=1.0,
                                                                default=(0.0, 0.0, 0.0, 0.0), subtype='COLOR', )

# textures Prefix properties
bpy.types.Scene.set_prefix_name = bpy.props.StringProperty(name='Prefix Name',
                                                           description='Name to set before the generated images',
                                                           default='Prefix Name')
bpy.types.Scene.set_res_width_prefix = bpy.props.IntProperty(name="Image Width", description="Width of prefix image",
                                                             default=2048)
bpy.types.Scene.set_res_height_prefix = bpy.props.IntProperty(name="Image Height", description="Height of prefix image",
                                                              default=2048)
bpy.types.Scene.set_prefix_color = bpy.props.FloatVectorProperty(name="Prefix Color",
                                                                 description="Color of generated image", size=4,
                                                                 min=0.0, max=1.0,
                                                                 default=(0.8, 0.8, 0.8, 1.0), subtype='COLOR', )

# textures light properties
bpy.types.Scene.set_tex1_name = bpy.props.StringProperty(name='Light Color',
                                                         description='Name to set before the generated images',
                                                         default='Light')
bpy.types.Scene.set_res_width_tex1 = bpy.props.IntProperty(name="Image Width", description="Width of Texture 1 image",
                                                           default=2048)
bpy.types.Scene.set_res_height_tex1 = bpy.props.IntProperty(name="Image Height",
                                                            description="Height of Texture 1 image",
                                                            default=2048)
bpy.types.Scene.set_tex1_color = bpy.props.FloatVectorProperty(name="Light Color",
                                                               description="Color of generated image", size=4, min=0.0,
                                                               max=1.0,
                                                               default=(0.0, 0.0, 0.0, 1.0), subtype='COLOR', )

# textures shadow properties
bpy.types.Scene.set_tex2_name = bpy.props.StringProperty(name='Shadow Color',
                                                         description='Name to set before the generated images',
                                                         default='Shadow')
bpy.types.Scene.set_res_width_tex2 = bpy.props.IntProperty(name="Image Width", description="Width of Texture 2 image",
                                                           default=2048)
bpy.types.Scene.set_res_height_tex2 = bpy.props.IntProperty(name="Image Height",
                                                            description="Height of Texture 2 image",
                                                            default=2048)
bpy.types.Scene.set_tex2_color = bpy.props.FloatVectorProperty(name="Shadow Color",
                                                               description="Color of generated image", size=4, min=0.0,
                                                               max=1.0,
                                                               default=(1.0, 1.0, 1.0, 1.0), subtype='COLOR', )

# textures shadow2 properties
bpy.types.Scene.set_tex3_name = bpy.props.StringProperty(name='Shadow Color2',
                                                         description='Name to set before the generated images',
                                                         default='Shadow 2')
bpy.types.Scene.set_res_width_tex3 = bpy.props.IntProperty(name="Image Width", description="Width of Texture 3 image",
                                                           default=2048)
bpy.types.Scene.set_res_height_tex3 = bpy.props.IntProperty(name="Image Height",
                                                            description="Height of Texture 3 image",
                                                            default=2048)
bpy.types.Scene.set_tex3_color = bpy.props.FloatVectorProperty(name="Shadow2 Color",
                                                               description="Color of generated image", size=4, min=0.0,
                                                               max=1.0,
                                                               default=(1.0, 1.0, 1.0, 1.0), subtype='COLOR', )

classes = (NPRPanel, NPRPanel2, NPRSetRes, NPRAddImg1, NPRAddImg2)

register, unregister = bpy.utils.register_classes_factory(classes)
