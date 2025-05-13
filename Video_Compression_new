import subprocess
import os

def compress_video(input_path, output_path, resolution):
    """
    压缩视频文件并指定分辨率
    :param input_path: 输入视频文件路径
    :param output_path: 输出视频文件路径
    :param resolution: 分辨率字符串（如"1280x720"）
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"输入文件 {input_path} 不存在")

    # 构造FFmpeg命令
    command = [
        "ffmpeg",
        "-i", input_path,                # 输入文件
        "-vf", f"scale={resolution}",    # 分辨率调整
        "-c:v", "libx264",               # H.264编码器
        "-crf", "23",                    # 视频质量（18-28，数值越小质量越高）
        "-preset", "medium",             # 编码速度预设
        "-c:a", "copy",                  # 音频直接复制（不重新编码）
        "-movflags", "+faststart",       # 优化流媒体播放
        output_path                      # 输出文件
    ]

    try:
        # 执行FFmpeg命令
        print(f"开始压缩视频：{input_path} → {output_path}")
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            raise Exception(f"FFmpeg执行失败：{result.stderr}")
        else:
            print("压缩完成！")
            print(f"输出文件：{output_path}")

    except Exception as e:
        print(f"发生错误：{str(e)}")

# 使用示例
if __name__ == "__main__":
    input_file = "input.mp4"
    output_file = "output.mp4"
    target_resolution = "1280x720"  # 可调整为其他分辨率（如"640x480", "1920x1080"）

    compress_video(input_file, output_file, target_resolution)
