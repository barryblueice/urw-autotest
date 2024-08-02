# urw-autotest：urwtest U盘/SSD测试工具批量化实现。

---

基于PyQt5打造的urwtest批量化实现。

**理论兼容：Win7/Win8/Win8.1/Win10**

目前支持功能：

- 单次跑圈（多盘）
- 多次跑圈（多盘，可指定次数）
  ~~（多次跑圈功能目前仍然存在不稳定因素，目前正在寻找解决方案）~~
- 展示本机所有磁盘
- 硬盘热插拔检测

---

### License:

**本项目遵照[GPL](https://www.gnu.org/licenses/gpl-3.0.en.html)协议开源。**

**不鼓励一切商用行为（包括司马lcb狗）。**

---

### 关于Issue：

在提交issue时，请详细描述你的操作，以便更快速的解决问题。

~~issue不清晰时有概率会引来祖安问候。~~

同时也可加入[QQ群](https://qm.qq.com/q/SQ6GrpdAQg)积极反馈Bug。

---

### 关于Releases & Build：

本项目在基本问题解决后即会发布Release。

**Release仅发布Windows版本。**

Release除源码外默认发布两个文件:

文件名 | 对应解释 | 备注
:---: | :---: | :---:
*_release_single.exe | 程序本体单文件版| 可能会出现普通版本不存在的特有Bug
*_release.zip | 程序本体压缩包 | 可执行主程序为urw_autotest.exe

你也可以通过[PyInstaller](https://pypi.org/project/pyinstaller/)或[Nuitka](https://pypi.org/project/Nuitka/)进行项目的可执行程序打包。

---

### Other:

由于QT5的显示问题，在部分启用了Windows缩放的显示器上会出现显示问题。

右键可执行文件-兼容性-属性-更改高DPI显示，选中替代高DPI缩放行为，缩放执行选择系统即可解决。