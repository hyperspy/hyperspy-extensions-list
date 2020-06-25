# (Known) HyperSpy extensions

HyperSpy extensions are packages that use the hyperspy extension mechanism to add functionality to HyperSpy (such as GUI widgets) and/or register new subclasses of HyperSpy objects (such as components and signals).

The following is a non-exhaustive list of HyperSpy extensions and the `signal_type` they provide:

| Package name                                                                   | Brief description                                                    | `signal_type`                                                    |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------|
| [hyperspy](https://github.com/hyperspy/hyperspy)                               | Core library                                                         | `EELS`, `EDS_TEM`, `EDS_SEM`, `DielectricFunction`, `hologram`   |
| [hyperspy-gui-ipywidgets](https://github.com/hyperspy/hyperspy_gui_ipywidgets) | ipywidgets widgets for HyperSpy                                      |                                                                  |
| [hyperspy-gui-traitsui](https://github.com/hyperspy/hyperspy_gui_traitsui)     | traitsui widgets for HyperSpy                                        |                                                                  |
| [KikuchiPy](https://github.com/kikuchipy/kikuchipy)                            | Processing and analysis of electron backscatter diffraction patterns | `EBSD`, `EBSDMasterPattern`, `VirtualBSEImage`                   |
| [pyXem](https://github.com/pyxem/pyxem)                                        | Multi-dimensional diffraction microscopy                             | `diffraction`, `electron_diffraction`, `diffraction_vectors`, `template_matching`, `vector_matching`, `crystallographic_map`, `vdf_image`, `reduced_intensity`, `diffraction_variance`, `dpc`, `correlation`, `power` |
| [lumispy](https://github.com/LumiSpy/lumispy)                                  | Processing and analysis of luminescence spectroscopy data            | `Luminescence`, `CL`, `CL_SEM`, `CL_STEM`, `EL`, `PL`            |

If you would like to add your package here, just send us a pull request.
