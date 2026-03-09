import os
import subprocess
import sys

def run_command(command):
    """运行终端命令并返回结果"""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败: {e.cmd}")
        print(f"错误信息: {e.stderr}")
        sys.exit(1)

def sync():
    print("🚀 开始自动化同步流程...")

    # 1. 导出本地数据 (排除不需要同步的内容)
    print("📦 正在导出本地博文数据...")
    run_command("python manage.py dumpdata blog --indent 2 > data.json")

    # 2. 提交到 Git
    print("🌿 正在提交更改到 GitHub...")
    run_command("git add data.json")
    # 允许 commit 失败（如果没有新更改）
    try:
        run_command('git commit -m "data: auto-sync blog posts"')
    except:
        print("⚠️ 没有检测到新内容，跳过提交")

    # 3. 推送到云端触发 Railway 部署
    print("📤 正在推送到云端...")
    run_command("git push")

    print("✅ 同步指令已发出！请等待 Railway 部署完成（约1-2分钟）。")

if __name__ == "__main__":
    sync()