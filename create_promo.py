import os
import sys
import glob
import subprocess
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=True):
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/mnt/c/Windows/Fonts/arialbd.ttf" if bold else "/mnt/c/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def create_intro_card(width, height, title, subtitle="", details=None):
    # Dark cyberpunk backdrop with gradient effect
    img = Image.new("RGB", (width, height), (14, 14, 18))
    draw = ImageDraw.Draw(img)

    # Outer decorative glow frame
    accent_color = (255, 107, 53) # #FF6B35 neon orange
    cyan_color = (0, 210, 106)    # Cyber green / cyan
    
    draw.rectangle([20, 20, width - 20, height - 20], outline=(40, 40, 52), width=3)
    draw.rectangle([26, 26, width - 26, height - 26], outline=accent_color, width=2)
    
    # Corner brackets
    corner_len = 35
    for (cx, cy) in [(20, 20), (width - 20, 20), (20, height - 20), (width - 20, height - 20)]:
        dx = corner_len if cx == 20 else -corner_len
        dy = corner_len if cy == 20 else -corner_len
        draw.line([(cx, cy), (cx + dx, cy)], fill=(255, 215, 0), width=6)
        draw.line([(cx, cy), (cx, cy + dy)], fill=(255, 215, 0), width=6)

    # Title
    font_title = get_font(68, bold=True)
    draw.text((width // 2, 130), title, font=font_title, fill=(255, 255, 255), anchor="mm")
    
    # Glow underline
    draw.line([(width // 2 - 180, 175), (width // 2 + 180, 175)], fill=accent_color, width=4)

    # Subtitle
    if subtitle:
        font_sub = get_font(26, bold=True)
        draw.text((width // 2, 215), subtitle, font=font_sub, fill=cyan_color, anchor="mm")

    # Details grid
    if details:
        y_start = 280
        box_w = width - 120
        box_x = 60
        draw.rounded_rectangle([box_x, y_start, box_x + box_w, y_start + 320], radius=16, fill=(22, 22, 30), outline=(50, 50, 65), width=2)

        font_label = get_font(22, bold=False)
        font_val = get_font(28, bold=True)
        
        row_h = 75
        for idx, (label, val, col) in enumerate(details):
            cy = y_start + 40 + idx * row_h
            # Label
            draw.text((box_x + 35, cy), label.upper(), font=font_label, fill=(160, 160, 180), anchor="lm")
            # Value
            draw.text((box_x + box_w - 35, cy), val, font=font_val, fill=col, anchor="rm")
            if idx < len(details) - 1:
                draw.line([(box_x + 30, cy + 36), (box_x + box_w - 30, cy + 36)], fill=(38, 38, 50), width=1)

    # Footer note
    font_foot = get_font(18, bold=False)
    draw.text((width // 2, height - 60), "404BOTS · TOP 100 RARE REVEAL", font=font_foot, fill=(110, 110, 130), anchor="mm")
    return img

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(base_dir, "top-100-collection", "images")
    promo_dir = os.path.join(base_dir, "promotion")
    os.makedirs(promo_dir, exist_ok=True)

    print(f"Checking images in: {img_dir}")
    if not os.path.exists(img_dir):
        print(f"Error: Images directory not found at {img_dir}")
        sys.exit(1)

    # Sort images by numerical rank (1.png to 100.png)
    image_files = []
    for i in range(1, 101):
        p = os.path.join(img_dir, f"{i}.png")
        if os.path.exists(p):
            image_files.append((i, p))
        else:
            # Check without leading zero or loose match
            matches = glob.glob(os.path.join(img_dir, f"*{i}.png"))
            if matches:
                image_files.append((i, matches[0]))

    if not image_files:
        print("No PNG images found in directory!")
        sys.exit(1)

    print(f"Found {len(image_files)} top-100 images.")

    # Target canvas size: 800x800
    target_size = (800, 800)
    w, h = target_size

    # 1. Generate Title Card
    card1 = create_intro_card(
        w, h,
        title="404BOT",
        subtitle="THE NEXT-GEN ALGORITHMIC NFT",
        details=[
            ("TOTAL SUPPLY", "2,222", (255, 215, 0)),
            ("BLOCKCHAIN", "ARC", (0, 220, 255)),
            ("MINT DATE", "TBA", (255, 107, 53)),
            ("MINT PRICE", "TBA", (170, 255, 0))
        ]
    )

    # 2. Transition Card: "Top 100 Showcase"
    card2 = create_intro_card(
        w, h,
        title="TOP 100 GRAILS",
        subtitle="UNVEILING THE 100 RAREST BOTS",
        details=[
            ("RARITY TIER", "TOP 100 LEGENDARY", (255, 215, 0)),
            ("PALETTES", "16 CHROMATIC THEMES", (0, 220, 255)),
            ("ACCESSORIES", "100% ULTRA-RARE", (255, 107, 53)),
            ("EFFECTS", "DYNAMIC GLITCH FX", (170, 255, 0))
        ]
    )

    # Save promo banner
    card1.save(os.path.join(promo_dir, "404bot_promo_banner.png"))
    print("Saved banner to promotion/404bot_promo_banner.png")

    # Build sequence of frames
    frames = []
    durations = []

    # Title card hold (2.0s = 20 frames at 100ms or hold duration)
    # For GIF, Pillow takes per-frame duration in ms
    frames.append(card1)
    durations.append(2200) # 2.2 seconds

    frames.append(card2)
    durations.append(1800) # 1.8 seconds

    font_overlay = get_font(20, bold=True)
    font_rank = get_font(24, bold=True)

    print("Compositing top 100 bot frames with branded overlays…")
    for rank, img_path in image_files:
        try:
            bot_img = Image.open(img_path).convert("RGBA")
            # If resized needed
            if bot_img.size != target_size:
                bot_img = bot_img.resize(target_size, Image.LANCZOS)
            
            # Composite onto dark background
            frame = Image.new("RGBA", target_size, (14, 14, 18, 255))
            frame.paste(bot_img, (0, 0), bot_img)

            # Draw bottom promo overlay pill
            draw = ImageDraw.Draw(frame)
            
            # Bottom banner bar
            bar_y = h - 68
            draw.rectangle([0, bar_y, w, h], fill=(10, 10, 14, 230))
            draw.line([(0, bar_y), (w, bar_y)], fill=(255, 107, 53), width=2)
            
            # Rank badge
            badge_text = f"★ RANK #{rank}"
            draw.rounded_rectangle([22, bar_y + 14, 175, bar_y + 54], radius=8, fill=(255, 107, 53))
            draw.text((98, bar_y + 34), badge_text, font=font_rank, fill=(255, 255, 255), anchor="mm")

            # Project specs in bottom bar
            specs_text = "SUPPLY: 2222  ·  CHAIN: ARC  ·  MINT: TBA"
            draw.text((w - 28, bar_y + 34), specs_text, font=font_overlay, fill=(210, 210, 225), anchor="rm")

            # Top branding subtle watermark
            draw.text((32, 32), "404BOT", font=get_font(20, bold=True), fill=(255, 255, 255, 120))
            draw.text((w - 32, 32), "TOP 100", font=get_font(18, bold=True), fill=(255, 215, 0, 160), anchor="rt")

            rgb_frame = frame.convert("RGB")
            frames.append(rgb_frame)
            # Duration per bot frame: 120ms (smooth, readable, high impact)
            durations.append(120)
        except Exception as e:
            print(f"Warning: could not process {img_path}: {e}")

    # Outro Card
    card_outro = create_intro_card(
        w, h,
        title="JOIN THE 404",
        subtitle="MINTING SOON ON ARC",
        details=[
            ("COLLECTION", "404BOT", (255, 255, 255)),
            ("TOTAL SUPPLY", "2,222 EDITIONS", (255, 215, 0)),
            ("CHAIN", "ARC NETWORK", (0, 220, 255)),
            ("STATUS", "MINT DATE & PRICE TBA", (255, 107, 53))
        ]
    )
    frames.append(card_outro)
    durations.append(3000) # 3.0s hold on outro

    # Save animated GIF
    gif_path = os.path.join(promo_dir, "404bot_promo.gif")
    print(f"\nEncoding animated GIF ({len(frames)} frames) to {gif_path}…")
    
    # Save GIF with optimized palette
    # Use 600x600 for web/Discord/Twitter GIF size optimization (<25MB limit)
    gif_size = (600, 600)
    resized_frames = [f.resize(gif_size, Image.BILINEAR).convert("P", palette=Image.ADAPTIVE, colors=128) for f in frames]
    
    resized_frames[0].save(
        gif_path,
        save_all=True,
        append_images=resized_frames[1:],
        duration=durations,
        loop=0,
        optimize=True
    )
    gif_size_mb = os.path.getsize(gif_path) / (1024 * 1024)
    print(f"✓ GIF successfully created: {gif_path} ({gif_size_mb:.2f} MB)")

    # Save frames for ffmpeg video generation
    frames_temp_dir = os.path.join(promo_dir, ".temp_frames")
    os.makedirs(frames_temp_dir, exist_ok=True)
    
    print("\nPreparing frames for MP4 video generation…")
    frame_idx = 0
    # Hold card1 for 2.2s (66 frames at 30fps)
    for _ in range(66):
        card1.save(os.path.join(frames_temp_dir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    # Hold card2 for 1.8s (54 frames at 30fps)
    for _ in range(54):
        card2.save(os.path.join(frames_temp_dir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    # Each bot: 4 frames at 30fps (~133ms)
    for f in frames[2:-1]:
        for _ in range(4):
            f.save(os.path.join(frames_temp_dir, f"frame_{frame_idx:05d}.png"))
            frame_idx += 1
    # Outro hold: 90 frames (3s at 30fps)
    for _ in range(90):
        card_outro.save(os.path.join(frames_temp_dir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1

    # Check if ffmpeg is available
    ffmpeg_cmd = None
    for cmd in ["ffmpeg", "/usr/bin/ffmpeg", "/usr/local/bin/ffmpeg"]:
        try:
            res = subprocess.run([cmd, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if res.returncode == 0:
                ffmpeg_cmd = cmd
                break
        except Exception:
            pass

    mp4_path = os.path.join(promo_dir, "404bot_promo.mp4")
    if ffmpeg_cmd:
        print(f"Encoding MP4 video with {ffmpeg_cmd}…")
        ff_run = subprocess.run([
            ffmpeg_cmd, "-y",
            "-framerate", "30",
            "-i", os.path.join(frames_temp_dir, "frame_%05d.png"),
            "-c:v", "libx264",
            "-profile:v", "high",
            "-crf", "20",
            "-pix_fmt", "yuv420p",
            mp4_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if ff_run.returncode == 0 and os.path.exists(mp4_path):
            mp4_size_mb = os.path.getsize(mp4_path) / (1024 * 1024)
            print(f"✓ MP4 video created: {mp4_path} ({mp4_size_mb:.2f} MB)")
    else:
        print("\nNote: ffmpeg is not currently installed. To render the MP4 video:")
        print("  sudo apt-get install -y ffmpeg")
        print(f"  ffmpeg -y -framerate 30 -i {frames_temp_dir}/frame_%05d.png -c:v libx264 -pix_fmt yuv420p {mp4_path}")

    # Clean up temp frames if MP4 was created
    if os.path.exists(mp4_path):
        for f in glob.glob(os.path.join(frames_temp_dir, "*.png")):
            try:
                os.remove(f)
            except Exception:
                pass
        try:
            os.rmdir(frames_temp_dir)
        except Exception:
            pass

    print("\n==========================================")
    print("PROMOTION ASSETS READY IN: promotion/")
    print(f" - GIF:    {gif_path}")
    if os.path.exists(mp4_path):
        print(f" - VIDEO:  {mp4_path}")
    print(f" - BANNER: {os.path.join(promo_dir, '404bot_promo_banner.png')}")
    print("==========================================")

if __name__ == "__main__":
    main()
