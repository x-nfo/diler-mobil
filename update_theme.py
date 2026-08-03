import sys

file_path = '/home/sandi/projects/template-car-dealer/index-v2.html'
with open(file_path, 'r') as f:
    content = f.read()

old_colors = """                    colors: {
                        ajm: {
                            navy: '#0B192C',
                            blue: '#3B82F6',
                            brightblue: '#60A5FA',
                            yellow: '#FBBF24',
                            yellowlight: '#FDE68A',
                            lightblue: '#EFF6FF',
                            slate: '#607D8B',
                            lightgray: '#F8FAFC',
                            success: '#4CAF50',
                            warning: '#FFC107',
                            danger: '#F44336',
                            info: '#2196F3'
                        }
                    },"""

new_colors = """                    colors: {
                        ajm: {
                            navy: '#002F6C',
                            blue: '#0057FF',
                            brightblue: '#4DA3FF',
                            orange: '#FF8C00',
                            orangelight: '#FFB84D',
                            lightblue: '#E6F1FF',
                            slate: '#95A3B8',
                            lightgray: '#F3F6FB',
                            success: '#00A651',
                            warning: '#FFB000',
                            danger: '#E63946',
                            info: '#0057FF',
                            secondary: '#6F42C1'
                        }
                    },"""

content = content.replace(old_colors, new_colors)

# Replace color classes
content = content.replace('ajm-yellowlight', 'ajm-orangelight')
content = content.replace('ajm-yellow', 'ajm-orange')

# Replace rgba values that matched the old yellow
content = content.replace('rgba(255,193,7,0.15)', 'rgba(255,140,0,0.15)')
content = content.replace('rgba(255,193,7,0.8)', 'rgba(255,140,0,0.8)')

# Update badge colors to use success theme
content = content.replace('bg-green-100 text-green-700', 'bg-ajm-success/10 text-ajm-success')
content = content.replace('bg-[#f8f9fa]', 'bg-ajm-lightgray')

with open(file_path, 'w') as f:
    f.write(content)

print("Theme updated successfully.")
