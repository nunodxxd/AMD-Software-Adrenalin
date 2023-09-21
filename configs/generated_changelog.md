## New Feature Highlights

* **New Game Support**
	+ Lies of P
	+ Party Animals
	+ The Crew™ Motorfest
* **Additional SDK Support**
	+ [Microsoft® Agility SDK Preview Release v1.711.3](https://devblogs.microsoft.com/directx/agility-sdk-1-711/) including Shader Model 6.8 functionality for Work Graphs, Wave Matric and AV1 Encode.
	+ [Microsoft® Agility SDK Retail Release 1.610.5](https://www.nuget.org/packages/Microsoft.Direct3D.D3D12/1.610.5) including Enhanced Barriers and Vulkan on DX12 compatibility features.
* **New AMD Radeon™ Anti-Lag+ Game Support**
	+ AMD Software: Adrenalin Edition 23.9.2 introduces Anti-Lag+ support for Starfield, Witcher 3, ELDEN RING and Immortal of Aveum™.
		- Up to 45% decrease in latency across select titles when AMD Radeon™ Anti-Lag+ is on, using AMD Software: Adrenalin Edition™️ 23.9.2 on the Radeon™ RX 7900 XTX GPU in select titles, versus when AMD Radeon Anti-Lag+ is off.RS-597
	+ AMD Radeon™ Anti-Lag+ features an onscreen overlay that can be used to display the system latency of supported games. When Anti-Lag+ is enabled, the onscreen overlay can be toggled on using ALT+SHIFT+L hotkey.
		- Toggling the hotkey will first enable the status indicator of Anti-Lag+ (a white triangle), and then display latency in ms or number of frames.
		- To compare the difference between Anti-Lag+ and Anti-Lag, hold the DEL key. To compare the difference between Anti-Lag+ On and Off, hold the right CTRL key.
		- Use the ALT+SHIFT+F hotkey to monitor FPS when Anti-Lag or Anti-Lag+ is enabled in the game.

## Fixed Issues

* Application crash may be observed while playing Baldur's Gate 3 with Vulkan® API set on some AMD Graphics Products, such as the Radeon™ RX 7900 XTX.
* GPU Clock may be artificially limited to 2700 MHz when performing manual tuning on Radeon™ RX 7700 XT and RX 7800 XT graphics.
* Display may not reach correct brightness with certain games on select SAMSUNG™ FreeSync Premium Pro monitors or TVs with local dimming setting enabled.
* Application crash or driver timeout may be observed while playing SMITE® on some AMD Graphics Products, such as the Radeon™ RX 7900 XTX.
* Intermittent application crash or driver timeout may be observed while playing F1® 23 on some AMD Graphics Products, such as the Radeon™ RX 7800 XT.

## Known Issues

* Performance Metrics Overlay may report N/A for FPS on various games.
* Audio may intermittently become out of sync with video when recording from AMD Software: Adrenalin Edition with AV1 codec.
* The display may intermittently freeze after changing the encoding format while streaming select games using AMD Link. Users experiencing this issue are suggested to select the desired encode format before streaming as a temporary workaround.

## SHA256 checksum:

 * amd-software-adrenalin-edition-23.9.2-combined-minimalsetup-230919\_web.exe: 3be3905644c8ef41239672534078992682f7e3826394439960e2871f04fd69fa
* whql-amd-software-adrenalin-edition-23.9.2-win10-win11-sep19-combined.exe: 3f3af2629b16bafd3ab0677456b1469fbe1c4057e0db96c10f81b3bb1cb8fce6

