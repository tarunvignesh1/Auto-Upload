import numpy as np
from moviepy.editor import ImageClip, VideoFileClip, concatenate_videoclips

def create_visual_effect_image(image_path, audio_clip, duration):
    image = ImageClip(image_path)
    # Set the duration of the image to match the audio duration
    image = image.set_duration(duration)

    def apply_visual_effect(t):
        # Calculate the audio amplitude at time 't'
        amplitude = audio_clip.get_frame(t)[0]

        # Scale the amplitude to the range [0, 255]
        scaled_amplitude = int((amplitude + 60) * 255 / 60)

        # Apply the color effect based on the scaled amplitude
        color = (255 - scaled_amplitude, scaled_amplitude, 128)

        # Create an image with the applied color effect
        visual_effect_image = image.copy().set_duration(0.1).set_pos(("center", "center")).set_opacity(0.8)
        visual_effect_image = visual_effect_image.set_duration(image.duration)

        return visual_effect_image.on_color(color)

    # Apply the visual effect for the entire image duration
    image_with_effect = image.fl(apply_visual_effect)

    return image_with_effect


from moviepy.editor import AudioFileClip

def create_audio_video(audio_path):
    audio_clip = AudioFileClip(audio_path)
    audio_video = audio_clip.to_ImageClip()
    return audio_video

def main(image_path, audio_path):
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    image_with_effect = create_visual_effect_image(image_path, audio_clip, audio_duration)
    audio_video = create_audio_video(audio_path)

    final_video = concatenate_videoclips([image_with_effect, audio_video], method="compose")
    final_video.write_videofile("output_video.mp4", codec="libx264")

main("downloaded_images/cute-anime-characters-from-dungeon-master-qg24kv9b68fcyero.jpg",)
