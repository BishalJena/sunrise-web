#!/usr/bin/env python3
"""Optimize screenshots to target size while maintaining quality and aspect ratio."""

from PIL import Image
import os

SCREENS_DIR = "tools/site-builder/screens"
TARGET_SIZE_KB = 300
TARGET_RATIO = 9 / 19.5  # iPhone aspect ratio

def optimize_image(filepath, target_kb=TARGET_SIZE_KB):
    """Optimize a PNG image to target file size."""
    size_kb = os.path.getsize(filepath) / 1024
    
    if size_kb <= target_kb:
        return False, size_kb, size_kb
    
    print(f"Optimizing {filepath} ({size_kb:.1f}KB -> target {target_kb}KB)")
    
    with Image.open(filepath) as img:
        # Check aspect ratio
        width, height = img.size
        ratio = width / height
        expected_width = int(height * TARGET_RATIO)
        
        if abs(ratio - TARGET_RATIO) > 0.01:
            print(f"  ⚠️  Warning: aspect ratio {ratio:.4f} differs from target {TARGET_RATIO:.4f}")
        
        # Try progressive quality reduction
        for quality in [95, 90, 85, 80, 75, 70, 65]:
            # Convert to RGB if necessary (for JPEG testing)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Keep as PNG for transparency support
                img.save(filepath, 'PNG', optimize=True)
                break
            else:
                # For RGB images, we can try both PNG optimization and conversion
                # First try optimized PNG
                temp_path = filepath + '.tmp'
                img.save(temp_path, 'PNG', optimize=True)
                new_size_kb = os.path.getsize(temp_path) / 1024
                
                if new_size_kb <= target_kb:
                    os.rename(temp_path, filepath)
                    print(f"  ✓ Optimized PNG: {size_kb:.1f}KB -> {new_size_kb:.1f}KB")
                    return True, size_kb, new_size_kb
                else:
                    os.remove(temp_path)
                    # If still too large, try WebP
                    temp_webp = filepath.replace('.png', '.webp.tmp')
                    img.save(temp_webp, 'WebP', quality=quality)
                    webp_size_kb = os.path.getsize(temp_webp) / 1024
                    
                    if webp_size_kb <= target_kb:
                        # Rename to .webp
                        webp_path = filepath.replace('.png', '.webp')
                        os.rename(temp_webp, webp_path)
                        os.remove(filepath)
                        print(f"  ✓ Converted to WebP: {size_kb:.1f}KB -> {webp_size_kb:.1f}KB")
                        return True, size_kb, webp_size_kb
                    else:
                        os.remove(temp_webp)
    
    # If all else fails, just optimize the PNG
    with Image.open(filepath) as img:
        img.save(filepath, 'PNG', optimize=True)
        new_size_kb = os.path.getsize(filepath) / 1024
        if new_size_kb < size_kb:
            print(f"  ✓ Optimized PNG: {size_kb:.1f}KB -> {new_size_kb:.1f}KB")
            return True, size_kb, new_size_kb
    
    return False, size_kb, size_kb

def main():
    """Optimize all screenshots."""
    apps = ["bersih", "hush", "kesha", "listo", "tldr-news"]
    
    total_saved = 0
    optimized_count = 0
    
    for app in apps:
        app_dir = os.path.join(SCREENS_DIR, app)
        if not os.path.exists(app_dir):
            continue
        
        print(f"\n=== {app.upper()} ===")
        
        for filename in sorted(os.listdir(app_dir)):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(app_dir, filename)
                optimized, old_size, new_size = optimize_image(filepath)
                
                if optimized:
                    saved = old_size - new_size
                    total_saved += saved
                    optimized_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: Optimized {optimized_count} files")
    print(f"Total space saved: {total_saved:.1f}KB")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
