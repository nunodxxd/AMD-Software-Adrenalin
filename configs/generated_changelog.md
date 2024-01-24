## New Feature Highlights

* **New Game Support**
	+ Like A Dragon: Infinite Wealth
	+ TEKKEN™ 8
* **New Product Support**
	+ AMD Radeon™ RX 7600 XT
* **AMD Fluid Motion Frames (AFMF) -** Boost FPS up to 97% for a smoother gaming experience by adding frame generation technology to **any** DirectX® 11 and 12 game. RS-630
	+ AFMF improves performance by adding frame generation technology to AMD Radeon™ 700M, RX 6000, and RX 7000 series GPUs for notebook and desktop platforms.
		- Up to 97% average increase in performance across select titles at 1080p resolution when AMD Fluid Motion Frames (AFMF) is ON and upscaled with FidelityFX™ Super Resolution 2 (FSR 2) at Quality Mode, using AMD Software: Adrenalin Edition™️ 24.1.1 on the Radeon™ RX 7600XT GPU, versus when AFMF and FSR 2 upscaling are OFF. RS-630
		- Up to 103% average increase in performance across select titles at 1440p resolution when AMD Fluid Motion Frames (AFMF) is ON and upscaled with FidelityFX™ Super Resolution 2 (FSR 2) at Quality Mode, using AMD Software: Adrenalin Edition™️ 24.1.1 on the Radeon™ RX 7600XT GPU, versus when AFMF and FSR 2 upscaling are OFF. RS-631
	+ AFMF preserves image quality by dynamically disabling frame generation during fast visual motion.
* **AMD Video Upscaling** – Advanced video upscale algorithm to improve video playback image quality for AMD Radeon™ RX 7000 desktop series GPUs.
	+ AMD Video Upscaling can be enabled within the Graphics tab to enjoy improved sharpness and clarity, for DirectX 11 applications such as Google Chrome, Microsoft Edge, and Media Player, with resolution support up to 4K.
	+ For more instructions on how to enable upscaling, please ensure that your version of AMD Software is up to date, and learn more [**HERE**](https://community.amd.com/t5/gaming/amd-software-24-1-1-amd-fluid-motion-frames-an-updated-ui-and/ba-p/656213)!
* **Additional Video Improvements**
	+ Content Adaptive Machine Learning (CAML) text detection has been updated to support up to 4K gaming for even greater clarity.
	+ Various encoding support within AMD Software including AVC, HEVC and AV1 codecs have undergone additional optimizations to improve video encode quality.
	+ AMD continues to work with partners to implement video enhancements into 3rd party apps; more updates to follow in upcoming drivers.
* **AMD Smart Technology Tab** – Access the suite of great A+A features from one convenient location to maximize the power of your AMD-powered system.
* **AMD Assistant** – Automatically enable or disable AMD Software features based on various situations for improved performance or battery life.
* **Additional OS Feature Support**
	+ Support for Hardware Accelerated GPU Scheduling has been expanded to Radeon™ RX 7600 series GPUs on Windows 11 version 22H2 and newer. Click [HERE](https://devblogs.microsoft.com/directx/hardware-accelerated-gpu-scheduling/) for more information.

## What to Know

* **AMD Fluid Motion Frames (AFMF)**
	+ AFMF can be enabled for **any** DirectX® 11 and 12 title using HYPR-RX.
		- AFMF may introduce additional latency to games and may not offer the optimal experience for fast-paced competitive titles. AFMF is recommended to be combined with AMD Radeon™ Anti-Lag to reduce in-game latency while maintaining a minimum in-game fps of 60.
		- Due to the potential latency impact of AFMF, it must be manually enabled in the per-game settings for certain fast-paced competitive titles, even if AFMF was already enabled globally. Gamers are free to enable AFMF in these titles based on their preference and gameplay style, however, they may not experience optimal performance – specifically at lower frame rates.
		- AFMF may be enabled or disabled on the fly using the default hotkey of Alt-Shift-G.
	+ AFMF currently requires the game to be played in fullscreen mode with VSYNC disabled.
		- For better compatibility with borderless-fullscreen titles, Windows 11 users can enable ["Optimizations for windowed games"](https://support.microsoft.com/en-us/windows/optimizations-for-windowed-games-in-windows-11-3f006843-2c7e-4ed0-9a5e-f9389e535952).
		- For a better visual experience, AFMF is recommended to be used with variable refresh rate enabled.
	+ Users can check AFMF’s frame generation status using AMD Software: Adrenalin Edition™’s in-game overlay.
	+ AFMF adds frame generation technology to boost FPS outside the game’s engine. Users can use AMD Software Performance Metrics Overlay to see the resulting FPS.
		- Support for third-party performance monitoring tools is not available at this moment.
	+ For systems setup using Hybrid Graphics (such as laptops featuring an integrated and discrete GPU), AFMF must be supported on the displaying GPU to be activated.
	+ Stay tuned for future enhancements and innovations coming to HYPR-RX with AFMF, focusing on elevating image quality, smoothness, and latency. Enjoy gaming with HYPR-RX.**AMD Video Upscaling**
	+ AMD Video Upscaling can be enabled for most DirectX 11 applications to improve image quality. However, certain applications such as Google Chrome and Microsoft Edge may require an additional step to activate AMD Video Upscaling.
		- For Google Chrome and Microsoft Edge, 'Media Foundation for Clear' must be enabled. This setting can be configured in the browser settings accessed through chrome://flags/ or edge://flags/.
	+ Users have the flexibility to adjust the level of sharpness added by AMD Video Upscaling using the slider located within the Graphics tab.
* **AMD Technical Preview Driver**
	+ Users had the opportunity to get an early look of AFMF through the AMD Technical Preview Drivers and provide their feedback to build and refine the feature. The feedback received through our online communities and [AMD Bug Report Tool](https://www.amd.com/en/support/kb/faq/amdbrt) helped create a more stable experience for AFMF in AMD Software: Adrenalin Edition 24.1.1.
	+ Users looking for updates of future AMD Technical Preview Drivers can subscribe to our newsletter [HERE](https://www.amd.com/en/forms/sign-up/gaming-software-news.html).

## Fixed Issues

* Performance drop may be observed in some DirectML workloads.
* Intermittent grey screen after driver upgrade with certain monitors (such as Nixeus NX-EDG274K) on Radeon™ RX 7000 series GPUs.
* Graphics API metric may show as N/A in certain UWP applications.
* Heavy stuttering may be experienced while playing Warframe and loading into a new area or starting a mission.
* Black artifacts may be observed in smoke effects while playing Call of Duty®: Modern Warfare® III.
* Black texture flickering may be observed while playing Starfield on some AMD Graphics Products, such as the Radeon™ RX 5600 XT.
* Intermittent install failure may be observed when using the factory reset setting.

## SHA256 checksum:

 * amd-software-adrenalin-edition-24.1.1-combined-minimalsetup-240122\_web.exe: e2766ad134d481a71ac7fbe0608175a74aa3df28d11fe4321245d38125576e7c
* whql-amd-software-adrenalin-edition-24.1.1-win10-win11-jan23-rdna.exe: 3577cb4b8ec827e6a465fb1502f3084f6de326753d29b81b9207b84d611a5117

