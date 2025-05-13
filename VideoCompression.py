import os
import subprocess
from pathlib import Path

def compress_videos(input_folder, output_folder, crf=23, preset='medium', target_size=None):
    """
    压缩多个视频文件
    
    参数:
    - input_folder: 输入视频文件夹路径
    - output_folder: 输出文件夹路径
    - crf: 压缩质量 (0-51, 0为无损, 23是默认值, 51质量最差)
    - preset: 编码速度与压缩率的平衡 (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)
    - target_size: 目标文件大小(MB), 如果指定则会自动调整比特率
    """
    # 确保输出文件夹存在
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # 支持的视频格式
    video_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')
    
    # 遍历输入文件夹
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(video_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            print(f"正在压缩: {filename}")
            
            if target_size:
                # 如果指定了目标大小，使用两遍编码来精确控制文件大小
                duration = float(subprocess.check_output(
                    f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 \"{input_path}\"",
                    shell=True).decode().strip())
                
                target_bitrate = int((target_size * 8192) / duration)  # 转换为kbps
                
                # 第一遍编码（分析）
                subprocess.call([
                    'ffmpeg', '-y', '-i', input_path,
                    '-c:v', 'libx264', '-preset', preset,
                    '-b:v', f'{target_bitrate}k', '-pass', '1',
                    '-f', 'mp4', '/dev/null' if os.name == 'posix' else 'NUL'
                ])
                
                # 第二遍编码（实际编码）
                subprocess.call([
                    'ffmpeg', '-y', '-i', input_path,
                    '-c:v', 'libx264', '-preset', preset,
                    '-b:v', f'{target_bitrate}k', '-pass', '2',
                    '-c:a', 'aac', '-b:a', '128k',
                    output_path
                ])
            else:
                # 使用CRF进行压缩（固定质量）
                subprocess.call([
                    'ffmpeg', '-i', input_path,
                    '-c:v', 'libx264', '-crf', str(crf), '-preset', preset,
                    '-c:a', 'aac', '-b:a', '128k',
                    output_path
                ])
            
            print(f"完成压缩: {filename}")

if __name__ == "__main__":
    # 使用示例
    input_dir = "input_videos"  # 输入视频文件夹
    output_dir = "compressed_videos"  # 输出文件夹
    
    # 方法1: 使用CRF控制质量 (推荐)
    compress_videos(input_dir, output_dir, crf=28)  # 更高的CRF值意味着更大的压缩
    
    # 方法2: 指定目标文件大小 (例如10MB)
    # compress_videos(input_dir, output_dir, target_size=10)
