import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_hero = """    <section id="home" class="relative pt-6 pb-20 min-h-[90vh] lg:min-h-screen flex items-center z-10 w-full overflow-hidden bg-[#1f2129] flex-col">
        <!-- Background Image -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
            <img src="https://images.unsplash.com/photo-1541892809226-9d3326759714?q=80&w=2000&auto=format&fit=crop" alt="Wrecked Car" class="w-full h-full object-cover opacity-30 grayscale mix-blend-luminosity">
            <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-[#050505]"></div>
        </div>

        <!-- Custom Header -->
        <div class="relative z-40 w-full flex justify-center px-4 mt-20 md:mt-10">
            <div class="flex items-center bg-gray-200/90 dark:bg-[#1a1a1a]/90 rounded-full p-1 shadow-lg backdrop-blur-md border border-white/10">
                <div class="w-10 h-10 bg-[#1a1a1a] dark:bg-black rounded-full flex items-center justify-center shadow-inner">
                    <span class="text-[#ccff00] font-bold text-xl leading-none">M</span>
                </div>
                <a href="https://wa.me/6287888087542" class="bg-[#1a1a1a] dark:bg-dash-red text-white text-[13px] font-bold px-6 py-2.5 rounded-full ml-1 hover:bg-black dark:hover:bg-red-700 transition-colors shadow-sm">
                    Hubungi WhatsApp
                </a>
            </div>
        </div>

        <!-- Hero Content -->
        <div class="relative z-10 w-full max-w-[1200px] mx-auto px-4 pt-32 pb-16 md:pt-48 md:pb-32 flex-1 flex flex-col justify-center">
            <div class="inline-flex items-center gap-2 border border-white/20 rounded-full px-4 py-2 mb-5 bg-black/40 backdrop-blur-md shadow-ambient w-max">
                <div class="w-2 h-2 rounded-full bg-blue-500 shadow-[0_0_8px_rgba(59,130,246,0.8)]"></div>
                <span class="text-[10px] md:text-[11px] font-bold text-blue-300 tracking-widest uppercase">Layanan Premium</span>
            </div>
            
            <h1 class="text-4xl md:text-6xl lg:text-7xl font-black text-white leading-[1.1] tracking-tight mb-5 md:mb-6 font-heading uppercase">
                Mobil Bekas Tabrak<br>
                <span class="text-[#ccff00]">Langsung jual</span>
            </h1>
            
            <p class="text-gray-300 text-[15px] md:text-lg max-w-[320px] md:max-w-2xl leading-relaxed font-medium md:font-light font-body">
                Rusak ringan, berat, hingga total loss (bangkai). Kami angkut dengan Towing GRATIS tanpa potongan biaya apapun.
            </p>
        </div>

        <!-- Overlapping Bottom Card (Search/Sell Toggle) -->
        <div class="absolute bottom-0 left-0 w-full z-30 translate-y-1/2 md:translate-y-1/3 px-4 flex justify-center">
            <div class="bg-white dark:bg-dash-screen rounded-[32px] md:rounded-[40px] pt-8 px-5 md:px-10 pb-16 w-full max-w-[1200px] shadow-[0_-10px_40px_rgba(0,0,0,0.2)] border border-gray-100 dark:border-white/10">
                <!-- Tabs/Toggle -->
                <div class="bg-gray-50 dark:bg-dash-panel p-1.5 rounded-2xl flex items-center mb-8 border border-gray-100 dark:border-white/5 max-w-[360px] md:max-w-[400px]">
                    <button class="flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-gray-400 font-semibold transition-colors hover:text-gray-600 dark:hover:text-white">
                        <i class="ph ph-magnifying-glass text-[20px]"></i>
                        <span class="text-sm">Cari Mobil</span>
                    </button>
                    <button class="flex-1 flex items-center justify-center gap-2 py-3 bg-white dark:bg-dash-red rounded-xl text-gray-900 dark:text-white font-bold shadow-[0_4px_12px_rgba(0,0,0,0.06)] border border-gray-100 dark:border-red-900 transition-colors">
                        <i class="ph-bold ph-money text-[20px]"></i>
                        <span class="text-sm font-heading">Jual Mobil</span>
                    </button>
                </div>
                
                <h2 class="text-[26px] md:text-4xl font-black text-gray-900 dark:text-white tracking-tight leading-[1.2] md:leading-tight max-w-[300px] md:max-w-xl font-heading uppercase">
                    Tiga Langkah Mudah Menjual Mobil Anda
                </h2>
            </div>
        </div>
    </section>
    
    <!-- Spacer to account for overlapping card -->
    <div class="h-32 md:h-40 bg-transparent dark:bg-[#050505] w-full"></div>
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<section id="home"' in line and start_idx == -1:
        start_idx = i
    elif '</section>' in line and start_idx != -1 and end_idx == -1:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    lines = lines[:start_idx] + [new_hero + "\n"] + lines[end_idx+1:]
    with open("index.html", "w") as f:
        f.writelines(lines)
    print(f"Successfully replaced lines {start_idx+1} to {end_idx+1}")
else:
    print("Could not find section tags")

