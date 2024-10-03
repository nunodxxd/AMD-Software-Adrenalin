
## Highlights


* ### New Game Support


	+ Frostpunk 2
	+ God of War Ragnarök
	+ Warhammer 40,000: Space Marine 2
	+ The Sims™ 4 DirectX® 11 Update
* ### AMD Fluid Motion Frames (AFMF) 2


	+ A major advancement in frame generation technology for AMD HYPR\-RX.
		- **Lower Latency and Higher Performance**
			* AFMF 2 enhances fast\-paced gaming by significantly reducing frame generation latency and improving performance scaling through new modes.
		- **Fast Motion Optimization**
			* Enjoy smoother gameplay and higher FPS with improved frame generation consistency during fast motion.
		- **Improved Borderless\-Fullscreen Support**
			* Expanded display mode support for RDNA 3 series graphics products ensures compatibility with virtually all borderless fullscreen games.
		- **Expanded API Support**
			* AFMF 2 can now be enabled for any OpenGLNEW, VulkanNEW, DirectX® 11, and DirectX® 12 titles.
		- **Radeon™ Chill Interoperability**
			* AFMF 2 now supports Radeon™ Chill, providing a low\-latency FPS capping option.
		- **Optimized AMD Ryzen AI™ 300 Series Support**
			* AFMF 2 is optimized for an extensive list of AMD products, including AMD Ryzen AI™ 300 series processors. Learn more [HERE](https://community.amd.com/t5/gaming/maximizing-gaming-performance-on-amd-ryzen-ai-300-series-with/ba-p/704594).
	+ Check out our new blog [HERE](https://community.amd.com/t5/gaming/boost-gaming-performance-by-2-5x-with-amd-software-adrenalin/ba-p/711458 "https://community.amd.com/t5/gaming/boost-gaming-performance-by-2-5x-with-amd-software-adrenalin/ba-p/711458") to learn more about AFMF 2 and this driver release.
  
* ### AMD Radeon™ Anti\-Lag 2 Vulkan® Support for Counter\-Strike 2


	+ AMD Radeon™ Anti\-Lag 2 now supports the Vulkan® API, offering additional responsive gaming options. AMD Radeon™ Anti\-Lag 2 introduces an in\-game option to optimally pace frames, further reducing input lag on AMD RDNA™ architecture\-based graphics products.
		- Users looking for a way to measure response time can use our [Frame Latency Meter (FLM)](https://gpuopen.com/learn/frame-latency-meter-flm-1-0/) or the built\-in latency monitor in AMD Radeon™ Anti\-Lag 2\.
			* Use the ALT\+SHIFT\+L hotkey to enable the Radeon Anti\-Lag 2 Latency Monitor. Once activated, a small white chevron will appear in the top left corner of your display, indicating that it is enabled.
			* Use ALT\+SHIFT\+L again to cycle through the following Latency Monitor display options: No metrics, FPS only, FPS and latency (in ms), FPS and latency (in ms and frames), FPS and latency (in ms and frames) with a legend.
			* To compare the difference between Anti\-Lag 2 On and Anti\-Lag Off, hold the right CTRL key.
		- Check out our new blog [HERE](https://gpuopen.com/learn/integrating-amd-radeon-anti-lag-2-sdk-in-your-game/) to learn more about the AMD Radeon™ Anti\-Lag 2 SDK.


* ### Geometric Downscaling for Video


	+ Improved image quality by reducing artifacts during downscaled video playback.
		- Geometric Downscaling is supported on AMD Radeon™ 800M integrated graphics, as well as AMD Radeon™ RX 7000 series desktop and mobile discrete graphics cards.


* ### Expanded AMD Radeon™ Boost Support


	+ FINAL FANTASY XVI
* ### Expanded HYPR\-Tune Support


	+ HYPR\-Tune support allows HYPR\-RX to enable in\-game technologies like AMD FidelityFX™ Super Resolution and AMD Radeon™ Anti\-Lag 2\.
	+ Support has been added to automatically configure AMD FidelityFX™ Super Resolution 3 with frame generation in:
		- Black Myth: Wukong
		- Creatures of Ava
		- Frostpunk 2
		- God of War Ragnarök
	+ Support has been added to automatically configure AMD Radeon™ Anti\-Lag 2 in:
		- Ghost of Tsushima DIRECTOR'S CUT
* ### Expanded Vulkan Extensions Support


	+ [VK\_AMD\_anti\_lag](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_AMD_anti_lag.html)
	+ [VK\_KHR\_maintenance7](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_KHR_maintenance7.html)
	+ [VK\_KHR\_pipeline\_binary](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_KHR_pipeline_binary.html)
	+ [VK\_EXT\_shader\_object](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_shader_object.html)
	+ Click [HERE](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-VULKAN.html) for more information about other Vulkan® extension support.
  
* ### Mesh Nodes in Work Graphs via Microsoft Agility SDK 1\.715\.0 Preview


	+ Microsoft DirectX® 12 [Work Graphs with Mesh Nodes](https://devblogs.microsoft.com/directx/d3d12-mesh-nodes-in-work-graphs/) support for AMD Radeon™ RX 7000 Series graphics cards.
		- View our accompanying blog post on [GPUOpen](https://gpuopen.com/learn/work_graphs_mesh_nodes/work_graphs_mesh_nodes-intro/) to learn more about Mesh Nodes in Work Graphs and how to enable it.
		- Find our Work Graphs Mesh Nodes samples on [GitHub](https://github.com/search?q=topic%3Ameshnodes+org%3AGPUOpen-LibrariesAndSDKs&type=repositories).
  
* ### Fixed Issues and Improvements


	+ Intermittent driver timeout or application crash while playing *Warhammer 40,000: Space Marine 2*.
	+ Intermittent driver timeout or application crash during certain cutscenes while playing *FINAL FANTASY XVI* on some AMD Graphics Products, such as the Radeon™ RX 6600 XT.
	+ Overly dark shadows or desaturated colors may be observed while playing *Black Myth: Wukong* when Global Illumination is to Medium or higher.
	+ Intermittent in\-game corruption may be observed while playing *Ghost of Tsushima DIRECTOR'S CUT* with AMD Software: Adrenalin Edition™ Record \& Streaming and HDR enabled.
	+ AFMF may become inactive after enabling certain on\-screen overlays.
	+ AMD Software: Adrenalin Edition may unexpectedly initiate upon system wake from sleep mode.
	+ Audio and video may intermittently become out of sync while recording using the AV1 codec in AMD Software: Adrenalin Edition.


## What to Know?


**AMD Fluid Motion Frames (AFMF) 2**


AFMF is a state\-of\-the\-art frame generation technology exclusive to AMD. It enhances frame rates and gameplay smoothness and is integrated into AMD Software: Adrenalin Edition™. As part of [AMD HYPR\-RX](https://www.amd.com/en/products/software/adrenalin/hypr-rx.html), our one\-click performance solution, it delivers exceptional gaming experiences on AMD Radeon graphics cards.


* **How to Enable AFMF 2**
	+ AFMF 2 can be enabled for any OpenGLNEW, VulkanNEW, DirectX® 11, and 12 title using HYPR\-RX or the AMD Fluid Motion 2 Toggle.
		- AFMF 2 is supported on AMD Radeon™ 700M and 800M integrated graphics, as well as AMD Radeon™ RX 6000 and RX 7000 series desktop and mobile discrete graphics cards.
		- AFMF 2 currently requires the game to be played in exclusive or borderless fullscreen mode with VSync disabled.
			* For a better visual experience, use AFMF 2 with a variable refresh rate\-enabled display.
				+ Enabling Radeon™ Chill after AFMF will automatically set the FPS cap to reduce tearing.
		- Use the in\-game overlay (ALT\+R) in AMD Software: Adrenalin Edition™ to check AFMF’s frame generation status.
	+ AFMF 2 adds frame generation technology to boost FPS outside the game’s engine. Users can enable the AMD Software Performance Metrics Overlay to see the resulting FPS.  
	
		- Users looking for a way to measure the response time of games can make use of our [Frame Latency Meter (FLM).](https://gpuopen.com/learn/frame-latency-meter-flm-1-0/)
* **How to Optimize AFMF 2**  

	+ AFMF 2 introduces new modes that are automatically tuned for the best experience based on your configuration. These can be manually adjusted to your preferences if needed  
	
		- AFMF 2 adds a new “High” Search Mode setting for improved frame consistency during fast motion, enabled by default for resolutions of 2560x1440 and above.  
		
			* This reduces the jittering or stuttering encountered with AFMF 1 at higher resolutions.
	+ AFMF 2 adds a new Performance Mode setting to reduce frame\-generation overhead, enabled as “Performance” by default for integrated graphics products.
		- Integrated graphics users may switch back to the “Quality” performance preset for better frame\-generation quality during fast motion. The “Quality” preset is the default when using discrete graphics cards.
		- Users can manually enable this “Performance” mode on discrete graphics cards to hit even higher frame rates when GPU bound to maximize the FPS uplift.
	+ Users can find these tuning options within the “Advanced View” of HYPR\-RX.
* **AFMF 2 Support for Multi\-GPU Configurations**
	+ For any hybrid\-graphics configuration, AFMF 2 will use the displaying GPU for frame generation, allowing the render GPU to focus on the game.


## Known Issues


* Intermittent performance when entering certain areas while playing *DayZ*. \[Resolution targeted for 24\.10\.1]
* Intermittent driver timeout or crash may be observed while playing *Warhammer 40,000: Space Marine 2* on some AMD Graphics Products, such as the AMD Ryzen™ AI 9 HX 370\. Users experiencing this issue can enable Variable Graphics Memory in AMD Software: Adrenalin Edition as a temporary measure (AMD Software: Adrenalin Edition \-\> Performance \-\> Tuning \-\> Variable Graphics Memory).


## Important Notes


* AMD is collaborating with the developers of *Frostpunk 2* to resolve an intermittent issue causing in game flicker while using AMD Software: Adrenalin Edition Record and Stream.
* AMD is collaborating with the developers of *Warhammer 40,000: Space Marine 2* to resolve an intermittent issue causing black flickering around certain water areas


## Package Contents


* AMD Software: Adrenalin Edition 24\.9\.1 Driver Version 24\.20\.11\.01 for Windows® 10 and Windows® 11 (Windows Driver Store Version 32\.0\.12011\.1036\)


## The AMD Software: Adrenalin Edition 24\.9\.1 installation package can be downloaded from the following link:


By clicking the Download button, you are confirming that you have read and agreed to be bound by the terms and conditions of the [End User License Agreement](/amd/language-masters/zh-tw/resources/support-articles/amd-software-eula.html) (“EULA”).  If you do not agree to the terms and conditions of these licenses, you do not have a license to any of the AMD software provided by this download.  




* [AMD Software: Adrenalin Edition 24\.9\.1 Driver for Windows® 10 \& Windows® 11 64\-bit](https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-24.9.1-win10-win11-sep-rdna.exe)


Systems pairing RDNA series graphics products with Polaris or Vega series graphics products:


* [AMD Software: Adrenalin Edition 24\.9\.1 Driver Including Vega and Polaris Series Graphics Support for Windows® 10 \& Windows® 11 64\-bit](https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-24.9.1-win10-win11-sep-rdna-combined.exe)


## Installing AMD Software: Adrenalin Edition


For detailed instructions on how to correctly uninstall or install AMD Software: Adrenalin Edition, please refer to the following support resources:


* [How\-To Uninstall AMD Software on a Windows® Based System](/amd/language-masters/zh-tw/resources/support-articles/faqs/RSX2-UNINSTALL.html)
* [How\-To Install AMD Software on a Windows® Based System](/amd/language-masters/zh-tw/resources/support-articles/faqs/RSX2-INSTALL.html)


**NOTE**: This driver is not intended for use on AMD Radeon products running in Apple Boot Camp platforms. Users of these platforms should contact their system manufacturer for driver support. When installing AMD Software: Adrenalin Edition 24\.9\.1 for the Windows® operating system, the user must be logged on as Administrator, or have Administrator rights to complete the installation of AMD Software: Adrenalin Edition 24\.9\.1\. 




## Radeon Product Compatibility


AMD Software: Adrenalin Edition 24\.9\.1 is compatible with the following AMD Radeon products.




| Radeon™ RX 7900/7800/7700/7600 Series Graphics |
| --- |
| Radeon™ RX 6900/6800/6700/6600/6500/6400 Series Graphics |
| Radeon™ RX 5700/5600/5500/5300 Series Graphics |


## Mobility Radeon™ Product Compatibility


AMD Software: Adrenalin Edition 24\.9\.1 is a notebook reference graphics driver with limited support for system vendor specific features. 




| AMD Radeon™ RX 7900M/7800M/7600M Series Graphics |
| --- |
| AMD Radeon™ RX 6800M/6700M/6600M/6500M/6300M Series Graphics |
| AMD Radeon™ RX 5700M/5600M/5500M/5300M Series Graphics |


## ​​​​AMD Processors with Radeon Graphics Product Compatibility


#### Important Note for Laptop and All\-In\-One (AIO) PCs


AMD recommends OEM\-provided drivers which are customized and validated for their system\-specific features and optimizations.  

  

If you experience issues using the AMD Software: Adrenalin Edition driver package downloaded from AMD.com, please install the OEM\-provided drivers for full support and compatibility.  

  

AMD Software: Adrenalin Edition does not include support for handheld gaming devices.  Users should check with the OEM for device specific drivers.




| DESKTOP | MOBILE |
| --- | --- |
| AMD Ryzen™ Processors with Radeon™ Graphics | AMD Ryzen™ AI Series Processors with Radeon™ Graphics |
| AMD Ryzen™ PRO Processors | AMD Ryzen™ Processors with Radeon™ Graphics |
| AMD Athlon™ Processors with Radeon™ Graphics | AMD Ryzen™ PRO Processors |
| AMD Athlon™ PRO Processors | AMD Athlon™ Processors with Radeon™ Graphics |
|  | AMD Athlon™ PRO Processors |


## Compatible Operating Systems


AMD Software: Adrenalin Edition 24\.9\.1 is designed to support the following Microsoft® Windows® platforms. Operating System support may vary depending on your specific AMD Radeon product.


## WHQL Results




|  | **Status** |
| --- | --- |
| WHQL Test Suite Results | Passed |
| WHQL Microsoft Certification | Passed |


## SHA256 checksum:

 * whql\-amd\-software\-adrenalin\-edition\-24\.9\.1\-win10\-win11\-sep\-rdna.exe: 4b401a4067d02625cfc006c27a49d2cedf0f9ebac492980cb493dc6f48b2835b
* amd\-software\-adrenalin\-edition\-24\.9\.1\-minimalsetup\-241001\_web.exe: c4fddbafd0af1c4613e02fcf746f69efe3571c3ddea6557ea66c4da8c1705033

