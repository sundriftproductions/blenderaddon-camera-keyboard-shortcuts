#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

import bpy
import math

# Version History
# 1.0.0 - 2020-12-16: Created. Replaces Toggle Camera Background Images and adds shortcuts for interocular/convergence distance.
# 1.0.1 - 2020-12-31: Added camera_keyboard_shortcuts_toggle_3d_mode.
# 1.0.2 - 2021-01-25: Made convergence steps smaller. Also cycles between several convergence settings when you reeet the convergence (rather than one "normal distance" preset convergence value). This helps when working at various distances.
# 1.0.3 - 2021-08-24: Made convergence steps as well as interocular steps four times smaller. It helps when working close up on objects.
# 1.0.4 - 2022-08-07: Misc formatting cleanup before uploading to GitHub.

bl_info = {
    "name": "Camera Keyboard Shortcuts",
    "author": "Jeff Boller",
    "version": (1, 0, 4),
    "blender": (2, 93, 0),
    "location": "",
    "description": "is a Blender add-on that provides various labor-saving keyboard shortcuts mostly related to working with a stereoscopic Blender camera. If you model your objects in stereoscopic 3D (like, with a 3D monitor or using anaglyph glasses on a regular monitor), this add-on will most likely be useful. " \
                   "To toggle between 2D, anaglyph, and two line interlaced 3D modes, use this keyboard shortcut command: wm.camera_keyboard_shortcuts_toggle_3d_mode " \
                   "To toggle between 2D, anaglyph, and two line interlaced 3D modes from Python, use this command: bpy.ops.wm.camera_keyboard_shortcuts_toggle_3d_mode() " \
                   "To adjust the interocular or convergence distance for the current camera in the scene, use these keyboard shortcut commands: " \
                   "wm.camera_keyboard_shortcuts_interocular_distance_add " \
                   "wm.camera_keyboard_shortcuts_interocular_distance_subtract " \
                   "wm.camera_keyboard_shortcuts_interocular_distance_reset " \
                   "wm.camera_keyboard_shortcuts_convergence_distance_add " \
                   "wm.camera_keyboard_shortcuts_convergence_distance_subtract " \
                   "wm.camera_keyboard_shortcuts_convergence_distance_reset " \
                   "If you want to call these shortcuts manually from Python, use one of the following commands: " \
                   "bpy.ops.wm.camera_keyboard_shortcuts_interocular_distance_add() " \
                   "bpy.ops.wm.camera_keyboard_shortcuts_interocular_distance_subtract() " \
                   "bpy.ops.wm.camera_keyboard_shortcuts_interocular_distance_reset() " \
                   "bpy.ops.wm.camera_keyboard_shortcuts_convergence_distance_add() "\
                   "bpy.ops.wm.camera_keyboard_shortcuts_convergence_distance_subtract() " \
                   "bpy.ops.wm.camera_keyboard_shortcuts_convergence_distance_reset() " \
                   "To toggle the background images checkbox for the current camera in a scene, use this keyboard shortcut command: wm.camera_keyboard_shortcuts_toggle_background_images " \
                   "To toggle the background images checkbox from Python, use this command: bpy.ops.wm.camera_keyboard_shortcuts_toggle_background_images() "\
                   "To switch the background image alpha value between 1 and 0.6, use this keyboard shortcut command: wm.camera_keyboard_shortcuts_toggle_alpha " \
                   "To switch the background image alpha value from Python, use this command: bpy.ops.wm.camera_keyboard_shortcuts_toggle_alpha()",
    "wiki_url": "https://github.com/sundriftproductions/blenderaddon-camera-keyboard-shortcuts/wiki",
    "tracker_url": "https://github.com/sundriftproductions/blenderaddon-camera-keyboard-shortcuts",
    "category": "System"}

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

class WM_OT_camera_keyboard_shortcuts_interocular_distance_add(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_interocular_distance_add'
    bl_label = 'Camera Keyboard Shortcuts - Interocular Distance Add'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_interocular_distance_add()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_interocular_distance_add')
        if not bpy.context.scene.render.use_multiview:
            self.report({'ERROR'}, 'Stereoscopy not enabled')
            return {"CANCELLED"}
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                bpy.data.objects[obj.name].data.stereo.interocular_distance += 0.003125
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_interocular_distance_subtract(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_interocular_distance_subtract'
    bl_label = 'Camera Keyboard Shortcuts - Interocular Distance Subtract'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_interocular_distance_subtract()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_interocular_distance_subtract')
        if not bpy.context.scene.render.use_multiview:
            self.report({'ERROR'}, 'Stereoscopy not enabled')
            return {"CANCELLED"}
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                bpy.data.objects[obj.name].data.stereo.interocular_distance -= 0.003125
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_interocular_distance_reset(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_interocular_distance_reset'
    bl_label = 'Camera Keyboard Shortcuts - Interocular Distance Reset'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_interocular_distance_reset()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_interocular_distance_reset')
        if not bpy.context.scene.render.use_multiview:
            self.report({'ERROR'}, 'Stereoscopy not enabled')
            return {"CANCELLED"}
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                bpy.data.objects[obj.name].data.stereo.interocular_distance = 0.065
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_convergence_distance_add(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_convergence_distance_add'
    bl_label = 'Camera Keyboard Shortcuts - Convergence Distance Add'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_convergence_distance_add()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_convergence_distance_add')
        if not bpy.context.scene.render.use_multiview:
            self.report({'ERROR'}, 'Stereoscopy not enabled')
            return {"CANCELLED"}
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                bpy.data.objects[obj.name].data.stereo.convergence_distance += 0.00765625
                self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_convergence_distance_add: ' + str(truncate(bpy.data.objects[obj.name].data.stereo.convergence_distance, 2)))
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_convergence_distance_subtract(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_convergence_distance_subtract'
    bl_label = 'Camera Keyboard Shortcuts - Convergence Distance Subtract'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_convergence_distance_subtract()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_convergence_distance_subtract')
        if not bpy.context.scene.render.use_multiview:
            self.report({'ERROR'}, 'Stereoscopy not enabled')
            return {"CANCELLED"}
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                bpy.data.objects[obj.name].data.stereo.convergence_distance -= 0.00765625
                self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_convergence_distance_subtract: ' + str(truncate(bpy.data.objects[obj.name].data.stereo.convergence_distance, 2)))

        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_convergence_distance_reset(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_convergence_distance_reset'
    bl_label = 'Camera Keyboard Shortcuts - Convergence Distance Reset'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_convergence_distance_reset()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_convergence_distance_reset')
        if not bpy.context.scene.render.use_multiview:
            self.report({'ERROR'}, 'Stereoscopy not enabled')
            return {"CANCELLED"}
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                compare = truncate(bpy.data.objects[obj.name].data.stereo.convergence_distance, 2)
                self.report({'INFO'}, 'compare: ' + str(compare))
                if compare <= 0.10:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.125
                elif compare <= 0.125:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.15
                elif compare <= 0.15:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.175
                elif compare <= 0.175:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.20
                elif compare <= 0.20:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.25
                elif compare <= 0.25:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.30
                elif compare <= 0.30:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.35
                elif compare <= 0.35:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.40
                elif compare <= 0.40:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.80
                elif compare <= 0.80:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 1.60
                elif compare <= 1.60:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 1.95
                elif compare <= 1.95:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 0.10
                else:
                    bpy.data.objects[obj.name].data.stereo.convergence_distance = 1.95
                self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_convergence_distance_reset: ' + str(truncate(bpy.data.objects[obj.name].data.stereo.convergence_distance, 2)))
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_toggle_background_images(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_toggle_background_images'
    bl_label = 'Camera Keyboard Shortcuts - Toggle Background Images'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_toggle_background_images()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_toggle_background_images')
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA' and obj.name == bpy.context.scene.camera.name:
                bpy.data.objects[obj.name].data.show_background_images = not bpy.data.objects[obj.name].data.show_background_images
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_toggle_alpha(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_toggle_alpha'
    bl_label = 'Camera Keyboard Shortcuts - Toggle Alpha on Background Images'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_toggle_alpha()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_toggle_alpha')
        for img in bpy.context.scene.camera.data.background_images:
            if img.show_background_image:
                if img.alpha == 1:
                    img.alpha = 0.6
                else:
                    img.alpha = 1
        return {'FINISHED'}

class WM_OT_camera_keyboard_shortcuts_toggle_3d_mode(bpy.types.Operator):
    bl_idname = 'wm.camera_keyboard_shortcuts_toggle_3d_mode'
    bl_label = 'Camera Keyboard Shortcuts - Toggle 3D Mode'
    bl_description = 'Call bpy.ops.wm.camera_keyboard_shortcuts_toggle_3d_mode()'
    bl_options = {'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'wm.camera_keyboard_shortcuts_toggle_3d_mode')
        if not bpy.context.scene.render.use_multiview:
            # Turn on 3D and start with anaglyph
            bpy.context.scene.render.use_multiview = True
            bpy.ops.wm.set_stereo_3d(display_mode='ANAGLYPH')
            self.report({'INFO'}, '3D Mode: Anaglyph')
        else:
            # 3D is already turned on. Let's see where we are in the sequence.
            if bpy.context.window.stereo_3d_display.display_mode == 'ANAGLYPH':
                # Toggle over to being in interlace.
                bpy.ops.wm.set_stereo_3d(display_mode='INTERLACE', use_interlace_swap=False)
                self.report({'INFO'}, '3D Mode: Interlaced')
            elif bpy.context.window.stereo_3d_display.display_mode == 'INTERLACE':
                # Interlace is already turned on. See if we need to flip the interlace swap.
                if not bpy.context.window.stereo_3d_display.use_interlace_swap:
                    bpy.ops.wm.set_stereo_3d(display_mode='INTERLACE', use_interlace_swap=True)
                    self.report({'INFO'}, '3D Mode: Interlaced (Swapped L-R)')
                else:
                    bpy.context.scene.render.use_multiview = False
                    self.report({'INFO'}, '2D Mode')
            else:
                bpy.context.scene.render.use_multiview = False
                self.report({'INFO'}, '2D Mode')

        return {'FINISHED'}

def register():
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_interocular_distance_add)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_interocular_distance_subtract)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_interocular_distance_reset)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_convergence_distance_add)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_convergence_distance_subtract)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_convergence_distance_reset)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_toggle_background_images)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_toggle_alpha)
    bpy.utils.register_class(WM_OT_camera_keyboard_shortcuts_toggle_3d_mode)

def unregister():
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_interocular_distance_add)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_interocular_distance_subtract)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_interocular_distance_reset)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_convergence_distance_add)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_convergence_distance_subtract)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_convergence_distance_reset)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_toggle_background_images)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_toggle_alpha)
    bpy.utils.unregister_class(WM_OT_camera_keyboard_shortcuts_toggle_3d_mode)

if __name__ == "__main__":
    register()
