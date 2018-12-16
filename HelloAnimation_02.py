bl_info = {
    "name": "Skateboard Animation Add-on",
    "author" : "Script Flip // Credits: swift502",
    "version" : (1, 0, 0),
    "blender" : (2, 7, 9),
    "description" : "Personalize Skateboard Animations",    
    "category": "Armature",
    "support": "TESTING",
    "location" : "View 3D > Object Mode > Armature",
}

#Installationsverzeichnis: C:\Users\josch\AppData\Roaming\Blender Foundation\Blender\2.79\scripts\addons
import bpy
from bpy.types import Panel, Operator
class KlasseButton (Operator):
    bl_idname = 'my.function'
    bl_label = 'my function'
    
    def execute (self, context):
        bpy.ops.object.transform_apply(scale = True)
        self.report
        return {'FINISHED'}


class Animation (Operator):
    bl_idname = 'my.animation'
    bl_label = 'my animation'
    
    def execute (self, context):
        
        
        self.report
        return{'FINISHED'}
    

class AddCamera (Operator):
    bl_idname = 'my.addcamera'
    bl_label = 'my addcamera'
    
    def execute (self, context):
        scene = context.scene
        cam_data = bpy.data.cameras.new(name="cam")  
        cam_ob = bpy.data.objects.new(name="Kamerka", object_data=cam_data)  
        scene.objects.link(cam_ob)  
        cam_ob.location = (-6, 1, 2.5)  
        cam_ob.rotation_euler = (1.35,0,-1.176)  
        cam = bpy.data.cameras[cam_data.name]  
        cam.lens = 10
        self.report
        return {'FINISHED'}

 
class ToolPanel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Animation Properties'
    bl_context = 'objectmode'
    bl_category = 'jayanam'
    
    def draw (self, context):
        layout = self.layout
        row = layout.row()
        obj = context.object
        str_prop = 'Data for ' + obj.name
        row.label(text=str_prop)
        
        row = layout.row()
        row.prop(obj, 'scale', index = 0, text= 'Noch Scale/Length')
        
        row = layout.row()
        row.operator('my.function', text = 'Button')
        
        row = layout.row()
        row.operator('my.addcamera', text = 'Add Camera for Render')
        
       
#create class
class ClassNameHere(bpy.types.Operator):
    
    bl_idname = "pose.add_animation"
    bl_label = "Animate selected Armature"
    bl_options = {'REGISTER', 'UNDO'}
    
    height_value = bpy.props.IntProperty(
        name = "Height",
        description = "Total Height of the jump",
        default = 2,
        min = 1,
        soft_max = 10,
        )
        
    lenght = bpy.props.FloatProperty(
        name = "Lenght",
        description = "How far the jump is going to be",
        default = 5,
        min = 1,
        soft_max = 10,
        )
        
    revolution = bpy.props.IntProperty(
        name = "Revolution",
        description = "How many revolutions at the airtime",
        default = 0,
        min = 0,
        max = 3,
        )
    
    
    def execute (self, context):
        scene = context.scene
        diepose = bpy.context.scene.objects['Skate_Arm']
        bone = diepose.pose.bones['Con_Main']
        bone.rotation_euler =(0,0,0)
        bone.location = (0,0,0)
        frame_num = 0
        positions = (0,1,0),(0,2,0),(0,3,0.4),(0,4,1.6),(0,5,2),(0,6,0.2),(0,7,0)
        for position in positions:
            scene.frame_set(frame_num)
            bone.location = position
            bone.keyframe_insert(data_path="location", index =-1)
            frame_num += 24
        
        
        self.report
        return{'FINISHED'}
        
def register():
    print("Registering BSAnimator")
    bpy.utils.register_class(AddCamera)
    bpy.utils.register_class(KlasseButton)
    bpy.utils.register_class(ToolPanel)
    bpy.utils.register_class(ClassNameHere)
    

def unregister():
    print("Unregistering BSAnimator")
    bpy.utils.unregister_class(AddCamera)
    bpy.utils.unregister_class(KlasseButton)
    bpy.utils.unregister_class(ToolPanel)
    bpy.utils.unregister_class(ClassNameHere)
    
if __name__ == '__main__':
    register()
