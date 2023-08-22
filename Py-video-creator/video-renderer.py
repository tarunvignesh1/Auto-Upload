import os
import moviepy.editor as mp
import numpy as np

def resize_image(img, new_size):
    height_ratio = new_size[0] / img.shape[0]
    width_ratio = new_size[1] / img.shape[1]
    return np.resize(img, (new_size[0], new_size[1], img.shape[2]))

def video_creator(image_path, audio_path, output_path, duration):
    # Load the image
    image = mp.ImageClip(image_path).set_duration(duration)

    # Load the audio
    audio = mp.AudioFileClip(audio_path)
    audio_duration = min(duration, audio.duration)

    # Function to update the image's position based on audio amplitude
    def update_image(t):
        t = min(t, audio_duration)
        amplitude = audio.get_frame(t)[0]
        return image.set_position(("center", 0.5 + amplitude * 0.2), relative=True)

    # Create a video clip with the image reacting to audio
    video = mp.VideoClip(lambda t: update_image(t).get_frame(t), duration=duration)

    # Resize the video to 1080p (1920x1080) and render the video
    new_size = (1080, 1920)
    resized_image = resize_image(image.get_frame(0), new_size)
    video = video.fl_image(lambda img: resized_image)
    video = video.set_audio(audio)

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    video.write_videofile(output_path, fps=30, codec='libx264')




if __name__ == "__main__":
    image_folder = "downloaded_images"  # Replace with the actual path to your image
    audio_folder = "downloaded_videos"  # Replace with the actual path to your audio

    image_files = os.listdir(image_folder)
    audio_files = os.listdir(audio_folder)

    image_path = os.path.join(image_folder, image_files[0])
    audio_path = os.path.join(audio_folder, audio_files[0])

    output_path = "rendered_videos/output_video.mp4"

    clip = mp.AudioFileClip(audio_path)
    duration = clip.duration

    video_creator(image_path, audio_path, output_path, duration)
    clip = mp.VideoFileClip(output_path)