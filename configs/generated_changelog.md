## New Product Support

* AMD Radeon™ RX 9070 XT
* AMD Radeon™ RX 9070
* AMD Radeon™ RX 7650 GRE
* AMD Ryzen™ Al Max+ 395
* AMD Ryzen™ AI 5 PRO 340 (AMD Radeon™ 840M)
* AMD Ryzen™ AI 7 PRO 350 (AMD Radeon™ 860M)
* AMD Ryzen™ AI 5 340 (AMD Radeon™ 840M)
* AMD Ryzen™ Al 7 350 (AMD Radeon™ 860M)
* AMD Ryzen 9 9955HX with AMD Radeon™ Graphics
* AMD Ryzen 9 9850HX with AMD Radeon™ Graphics
* AMD Ryzen 9 9955HX3D with AMD Radeon™ Graphics
* AMD Ryzen 9 9955HX3D with AMD Radeon™ Graphics

## New Features

* **AMD Fidelity™ FX Super Resolution 4 (AMD FSR 4)**
  + Support is exclusively on AMD Radeon™ RX 9070 Series graphics cards.
  + AMD FSR 4 features a new upgrade toggle in AMD Software: Adrenalin Edition™ that automatically upgrades supported games that have built-in AMD FSR 3.1 support to use the new ML-based AMD FSR 4 upscaling algorithm.
  + AMD FSR 4 will be available for over 30 games on Radeon™ RX 9070 Series Graphics Cards. For more information, click [HERE](https://community.amd.com/t5/gaming/game-changing-updates-fsr-4-afmf-2-1-ai-powered-features-amp/ba-p/748504).
* **AMD Fluid Motion Frames 2.1**
  + Improved frame generation image quality with reduced ghosting and better temporal tracking.
  + Support for AMD Radeon™ RX 6000, 7000, 9070 series graphics cards and AMD Ryzen™ AI 300 Series processors
* **AI Enhanced Features in AMD Software: Adrenalin Edition™**
  + Support is exclusively on AMD Radeon™ RX 9070 Series graphics cards.
  + **AMD Chat**
    - AMD Chat is a GPU-accelerated, local offline chatbot with text and image generation capabilities.
    - AMD Chat can answer common questions about a user’s AMD hardware and enable key features in AMD Software: Adrenalin Edition™.
  + **AMD Image Inspector**
    - AMD Image Inspector leverages AI to help AMD accelerate game quality improvements by capturing text and image diagnostic data.
* **AMD Install Manager**
  + AMD Install Manager is a new application that easily manages your AMD specific software installations.
  + AMD Install Manager supports the installation of our new AMD Chat and the latest AMD Graphics and Chipset drivers.
  + Users now have an option to “Automatically keep AMD Software up to date”, allowing the AMD Install Manager to update their installed drivers and software on-the-fly.
* **AMD Radeon™ Image Sharpening 2**
  + Support is exclusively on AMD Radeon™ RX 9070 Series graphics cards.
  + Now updated to provide stronger, more responsive sharpening in more use cases.
  + AMD Radeon™ Image Sharpening 2 can now apply sharpening to games, videos or across the entire desktop.

## Other Highlights

* **New Game Support**
  + FragPunk
  + Split Fiction
* **AMD ROCm™ on WSL for AMD Radeon™ RX 7000 Series**
  + Official support for Windows Subsystem for Linux (WSL 2) enables users with supported hardware to run workloads with AMD ROCm™ software on a Windows system, eliminating the need for dual boot set ups.
  + The following has been added to WSL 2:
    - Official support for Llama3 8B (via vLLM) and Stable Diffusion 3 models.
    - Support for Hugging Face transformers.
    - Support for Ubuntu 24.04.
  + Find more information on ROCm on Radeon compatibility [here](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/compatibility/wsl/wsl_compatibility.html) and configuration of Windows Subsystem for Linux (WSL 2)[here](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/limitations.html#wsl-specific-issues).
* **AI Performance Improvements on AMD Radeon™ RX 7000 Series**
  + Performance improvements to the following use cases:
    - Up to 70% improvement on Adobe Lightroom AI enhance detail.
    - Up to 13% improvement on Adobe Lightroom Denoise.
    - Up to 40% improvement with Topaz Photo AI subtest.
    - Up to 10% improvement on DaVinci resolve AI cases.
* **Developer Updates**
  + New AMD machine-readable GPU Instruction Set Architectures (ISAs) specifications updated to support AMD RDNA™ 4 and RDNA™ 3.5 architecture graphics cards. [Learn more](https://gpuopen.com/machine-readable-isa/).
  + New open-source AMD Advanced Interactive Streaming (AIS) SDK [release](https://gpuopen.com/learn/building-better-applications-together-open-source-amd-advanced-interactive-streaming), designed from the ground up to transform streaming from passive viewing into an immersive experience and AMD Advanced Media Framework (AMF) SDK [updates](https://gpuopen.com/advanced-media-framework/).
  + AMD Radeon™ Developer Tool Suite (RDTS) update with support for AMD Radeon™ RX 9000 Series graphics cards coming soon. The RDTS includes the recently released Driver Experiments tool that enables low-level control over the behavior of AMD Software: Adrenalin Edition™ for developers. Stay tuned to GPUOpen news for the latest [news for developers](https://gpuopen.com/news/).
* **Expanded HYPR-RX Support**
  + HYPR-Tune support allows HYPR-RX to enable in-game technologies like AMD FidelityFX™ Super Resolution and AMD Radeon ™ Anti-Lag 2.
  + Support has been added to automatically configure AMD FidelityFX™ Super Resolution with frame generation in:
    - Farming Simulator 25
    - S.T.A.L.K.E.R. 2: Heart of Chornobyl
    - Silent Hill 2
* **Expanded Vulkan Extension Support**
  + [VK\_EXT\_depth\_clamp\_control](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_depth_clamp_control.html)
  + Click [HERE](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-VULKAN.html) for more information about other Vulkan® extension support.
* **Fixed Issues and Improvements**
  + HEVC encoding may not work as expected while using OBS Studio with Twitch Enhanced Broadcasting.
  + Intermittent driver timeout or crash may be observed while playing Warhammer 40,000: Space Marine 2 on some AMD Graphics Products, such as the AMD Ryzen™ AI 9 HX 370.)
  + Lower than expected performance may be observed in Delta Force on Radeon™ RX 7000 series graphics products.
  + Intermittent stutter may be observed while playing Marvel Rivals when AMD FidelityFX™ Super Resolution 3 frame generation is enabled.

## Known Issues

* Intermittent crash of AMD Software: Adrenalin Edition™ may be observed while playing Marvel's Spider-Man 2 or Ratchet & Clank: Rift Apart with AMD Image Inspector enabled. Users experiencing this issue are recommended to disable AMD Image Inspector as a temporary workaround.
* Lower than expected performance may be observed when using YouTube on the Microsoft Edge web browser immediately after a driver install. Users experiencing this issue are recommended to restart Microsoft Edge and relaunch YouTube as a temporary workaround.
* 3rd party tools that rely on our ADL SDK for detecting ROPs count will incorrectly report 64 ROPs, and we are looking to address this in a driver update post launch.
* Incorrect gamma is exhibited while playing Counter-Strike 2 and using MSAA x8 on Radeon™ RX 9070 series graphics products.
* AMD Software: Adrenalin Edition™ may not accurately report AMD FSR 4 enablement for Marvel's Spider-Man 2.
* Lower than expected performance may be observed while playing Assetto Corsa Competizione on Radeon™ RX 9000 series graphics products.
* Intermittent application crash may be observed in Indiana Jones and the Great Circle when settings are set to "Very Ultra" quality and Path Tracing is enabled. Users experiencing this issue are recommended to use the default Ray Tracing settings as a temporary workaround.
* After using the AMD Cleanup Utility for Windows®, the AMD Bug Report Tool may appear intermittently during a new driver install on AMD Ryzen™ 7000 and above series processors paired with AMD Graphics Products.
* After completing a driver upgrade on certain laptops, users may experience intermittent failures for the integrated camera to start. Users experiencing this issue are recommended to use the AMD Cleanup Utility for Windows® and use our previous recommended driver, available [here](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html "https://www.amd.com/en/resources/support-articles/release-notes/rn-rad-win-24-12-1.html").
* Limitations for Windows Subsystem for Linux (WSL 2) support can be found [here](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/limitations.html#release-known-issues).



## Package Contents

* AMD Software: Adrenalin Edition 25.3.1 Driver Version 24.30.31.03 for Windows® 10 and Windows® 11 (Windows Driver Store Version 32.0.13031.3015).

## The AMD Software: Adrenalin Edition 25.3.1 installation package can be downloaded from the following link:

By clicking the Download button, you are confirming that you have read and agreed to be bound by the terms and conditions of the [End User License Agreement](/zh-tw/resources/support-articles/amd-software-eula.html) (“EULA”).  If you do not agree to the terms and conditions of these licenses, you do not have a license to any of the AMD software provided by this download.

* [AMD Software: Adrenalin Edition 25.3.1 Driver for Windows® 10 & Windows® 11 64-bit](https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.3.1-win10-win11-march-rdna.exe)

Systems pairing RDNA series graphics products with Polaris or Vega series graphics products:

* [AMD Software: Adrenalin Edition 25.3.1 Driver Including Vega and Polaris Series Graphics Support for Windows® 10 & Windows® 11 64-bit](https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-25.3.1-win10-win11-march-rdna-combined.exe)

## Installing AMD Software: Adrenalin Edition

For detailed instructions on how to correctly uninstall or install AMD Software: Adrenalin Edition, please refer to the following support resources:

* [How-To Uninstall AMD Software on a Windows® Based System](/en/resources/support-articles/faqs/RSX2-UNINSTALL.html)
* [How-To Install AMD Software on a Windows® Based System](/en/resources/support-articles/faqs/RSX2-INSTALL.html)

**NOTE**: This driver is not intended for use on AMD Radeon products running in Apple Boot Camp platforms. Users of these platforms should contact their system manufacturer for driver support. When installing AMD Software: Adrenalin Edition 25.3.1 for the Windows® operating system, the user must be logged on as Administrator, or have Administrator rights to complete the installation of AMD Software: Adrenalin Edition 25.3.1.

## Radeon Product Compatibility

AMD Software: Adrenalin Edition 25.3.1 is compatible with the following AMD Radeon products.

|  |
| --- |
| Radeon™ RX 9070 Series Graphics |
| Radeon™ RX 7900/7800/7700/7650/7600 Series Graphics |
| Radeon™ RX 6900/6800/6700/6600/6500/6400 Series Graphics |
| Radeon™ RX 5700/5600/5500/5300 Series Graphics |

## Mobility Radeon™ Product Compatibility

AMD Software: Adrenalin Edition 25.3.1 is a notebook reference graphics driver with limited support for system vendor specific features.

|  |
| --- |
| AMD Radeon™ RX 7900M/7800M/7600M Series Graphics |
| AMD Radeon™ RX 6800M/6700M/6600M/6500M/6300M Series Graphics |
| AMD Radeon™ RX 5700M/5600M/5500M/5300M Series Graphics |

## ​​​​AMD Processors with Radeon Graphics Product Compatibility

#### Important Note for Laptop and All-In-One (AIO) PCs

AMD recommends OEM-provided drivers which are customized and validated for their system-specific features and optimizations.  
  
If you experience issues using the AMD Software: Adrenalin Edition driver package downloaded from AMD.com, please install the OEM-provided drivers for full support and compatibility.  
  
AMD Software: Adrenalin Edition does not include support for handheld gaming devices.  Users should check with the OEM for device specific drivers.

| DESKTOP | MOBILE |
| --- | --- |
| AMD Ryzen™ Processors with Radeon™ Graphics | AMD Ryzen™ AI Series Processors with Radeon™ Graphics |
| AMD Ryzen™ PRO Processors | AMD Ryzen™ Processors with Radeon™ Graphics |
| AMD Athlon™ Processors with Radeon™ Graphics | AMD Ryzen™ PRO Processors |
| AMD Athlon™ PRO Processors | AMD Athlon™ Processors with Radeon™ Graphics |
|  | AMD Athlon™ PRO Processors |

## Compatible Operating Systems

AMD Software: Adrenalin Edition 25.3.1 is designed to support the following Microsoft® Windows® platforms. Operating System support may vary depending on your specific AMD Radeon product.

## WHQL Results

|  |  |
| --- | --- |
|  | **Status** |
| WHQL Test Suite Results | Passed |
| WHQL Microsoft Certification | Passed |

## SHA256 checksum:

* whql-amd-software-adrenalin-edition-25.3.1-win10-win11-march-rdna.exe: 21f6e960185fbf01cd46d17af54c47c1a0a1921248c1ad3e891d5d07ea166cb6
* amd-software-adrenalin-edition-25.3.1-minimalsetup-250305\_web.exe: 8a773c658bdd167454a4e7ffdb95100c005f073a2dc8d89ea63b02ba9bead0b3
* whql-amd-software-adrenalin-edition-25.3.1-win10-win11-march-rdna-combined.exe: 8859b39e3520a9d7f0fed3a25134407c63926ff404d806d53965d4206cdcb62b
