import math
from random import random

import numpy as np
import pnavpy.entity as entity
from pyray import *

init_window(800, 450, "Hello Pyray")
set_target_fps(60)

target_mesh = load_model_from_mesh(gen_mesh_sphere(5, 32, 32))
missile_mesh = load_model_from_mesh(gen_mesh_sphere(5, 32, 32))
camera = Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

def update_scene(scene, dt):
    camera = scene["camera"]
    target = scene["target"]
    missile = scene["missile"]

    update_camera(camera, CameraMode.CAMERA_ORBITAL)
    camera.target = tuple(missile.get_position())
    target_velocity = target.get_velocity()
    target_acceleration = target.get_acceleration()
    target_velocity_norm = target_velocity / np.linalg.norm(target_velocity)
    target_acceleration_norm = target_acceleration / np.linalg.norm(target_acceleration)
    camera.position = tuple(target.get_position() - (target_velocity_norm + target_acceleration_norm) * 10 + np.array([0.0, 1.0, 0.0]) * 5)

    offset = target.get_position() - missile.get_position()
    distance = np.linalg.norm(offset)

    target.update(dt)
    missile.update(dt)

    return distance > 1.0

def draw_scene(scene):
    target = scene["target"]
    missile = scene["missile"]
    draw_line_3d(tuple(missile.get_position()), tuple(missile.get_position() + missile.get_acceleration()), GREEN)
    draw_model(target_mesh, tuple(target.get_position()), 0.1, BLUE)
    draw_model(missile_mesh, tuple(missile.get_position()), 0.1, RED)

def create_scene():
    target_init = {
        "position": np.array([-10.0, 0.0, 0.0]),
        "velocity": np.array([3.0, 0.0, 0.0]),
        "acceleration": np.array([2.0, 0.0, 0.0])
    }

    target = entity.Projectile(
        target_init["position"],
        target_init["velocity"],
        target_init["acceleration"],
    )

    missile_init = {
        "postiion": np.array([10.0, 0.0, -10.0]),
        "velocity": np.array([0.0, 0.0, 0.5]),
    }

    missile = entity.SimpleSeekProjectile(
        postiion=missile_init["postiion"],
        velocity=missile_init["velocity"],
        target=target
    )

    return {
        "missile": missile,
        "target": target,
        "camera": camera
    }

def start():
    scene = create_scene()
    init_time = get_time()
    max_duration = 5

    while not window_should_close():
        now = get_time()
        finished = not update_scene(scene, get_frame_time())

        if now - init_time > max_duration or finished:
            scene = create_scene()
            init_time = now

        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode_3d(camera)

        draw_grid(10000, 1.0)
        draw_scene(scene)

        end_mode_3d()

        end_drawing()
    close_window()

if __name__ == '__main__':
    start()
