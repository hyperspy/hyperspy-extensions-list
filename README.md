
This repository contains a list of [HyperSpy](https://hyperspy.org)
extensions. HyperSpy extensions are packages that use the HyperSpy extension
mechanism to add functionality to HyperSpy (such as GUI widgets) and/or
register new subclasses of HyperSpy objects (such as components and signals).

# Adding a HyperSpy extension to the list

Note that the information in this file is automatically generated. To add a
package just [open an
issue](https://github.com/hyperspy/hyperspy-extensions-list/issues) with the
request and we'll get it done for you. Alternatively, [follow these
instructions](https://github.com/hyperspy/hyperspy-extensions-list/blob/master/doc/how_to_add_extension.md)
and send us a pull request.

# (Known) HyperSpy extensions

| Package name                                                                   | Brief description                                                    |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [hyperspy-gui-ipywidgets](https://github.com/hyperspy/hyperspy_gui_ipywidgets) | ipywidgets widgets for HyperSpy                                      |
| [hyperspy-gui-traitsui](https://github.com/hyperspy/hyperspy_gui_traitsui)     | traitsui widgets for HyperSpy                                        |
| [KikuchiPy](https://github.com/kikuchipy/kikuchipy)                            | Processing and analysis of electron backscatter diffraction patterns |
| [LumiSpy](https://github.com/lumispy/lumispy)                                  | Analysis of luminescence spectroscopy data                           |
| [pyxem](https://github.com/pyxem/pyxem)                                        | Multi-dimensional diffraction microscopy                             |

## List of `signal_type`'s provided by the different HyperSpy extensions in alphabetical order


<table>
    <thead>
        <tr>
            <th>signal_type</th>
            <th>aliases</th>
            <th>class name</th>
            <th>package</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CL_SEM</td>
            <td>CLSEM, cathodoluminescence SEM</td>
            <td>CLSEMSpectrum</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>CL_STEM</td>
            <td>CLSTEM, cathodoluminescence STEM</td>
            <td>CLSTEMSpectrum</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>CL</td>
            <td>CLSpectrum, cathodoluminescence</td>
            <td>CLSpectrum</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>TRCL</td>
            <td>TR cathodoluminescence, time-resolved cathodoluminescence</td>
            <td>CLTransient</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>correlation</td>
            <td></td>
            <td>Correlation2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>dpc</td>
            <td></td>
            <td>DPCBaseSignal</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>dpc</td>
            <td></td>
            <td>DPCSignal1D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>dpc</td>
            <td></td>
            <td>DPCSignal2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>DielectricFunction</td>
            <td>dielectric function</td>
            <td>DielectricFunction</td>
            <td>hyperspy</td>
        </tr>
        <tr>
            <td>diffraction</td>
            <td></td>
            <td>Diffraction1D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>diffraction</td>
            <td></td>
            <td>Diffraction2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>diffraction_variance</td>
            <td></td>
            <td>DiffractionVariance1D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>diffraction_variance</td>
            <td></td>
            <td>DiffractionVariance2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>diffraction_vectors</td>
            <td></td>
            <td>DiffractionVectors</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>diffraction_vectors</td>
            <td></td>
            <td>DiffractionVectors2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>tensor_field</td>
            <td></td>
            <td>DisplacementGradientMap</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>EBSD</td>
            <td>electron_backscatter_diffraction</td>
            <td>EBSD</td>
            <td>kikuchipy</td>
        </tr>
        <tr>
            <td>EBSDMasterPattern</td>
            <td>ebsd_masterpattern, masterpattern</td>
            <td>EBSDMasterPattern</td>
            <td>kikuchipy</td>
        </tr>
        <tr>
            <td>EDS_SEM</td>
            <td></td>
            <td>EDSSEMSpectrum</td>
            <td>hyperspy</td>
        </tr>
        <tr>
            <td>EDS_TEM</td>
            <td></td>
            <td>EDSTEMSpectrum</td>
            <td>hyperspy</td>
        </tr>
        <tr>
            <td>EELS</td>
            <td>TEM EELS</td>
            <td>EELSSpectrum</td>
            <td>hyperspy</td>
        </tr>
        <tr>
            <td>EL</td>
            <td>ELSpectrum, electroluminescence</td>
            <td>ELSpectrum</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>electron_diffraction</td>
            <td></td>
            <td>ElectronDiffraction1D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>electron_diffraction</td>
            <td></td>
            <td>ElectronDiffraction2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>hologram</td>
            <td></td>
            <td>HologramImage</td>
            <td>hyperspy</td>
        </tr>
        <tr>
            <td>Luminescence</td>
            <td>LuminescenceSpectrum</td>
            <td>LumiSpectrum</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>Luminescence</td>
            <td>TRLumi, TR luminescence, time-resolved luminescence</td>
            <td>LumiTransient</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>PL</td>
            <td>PLSpectrum, photoluminescence</td>
            <td>PLSpectrum</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>TRPL</td>
            <td>TR photoluminescence, time-resolved photoluminescence</td>
            <td>PLTransient</td>
            <td>lumispy</td>
        </tr>
        <tr>
            <td>pair_distribution_function</td>
            <td></td>
            <td>PairDistributionFunction1D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>polar_diffraction</td>
            <td></td>
            <td>PolarDiffraction2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>power</td>
            <td></td>
            <td>Power2D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>reduced_intensity</td>
            <td></td>
            <td>ReducedIntensity1D</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>template_matching</td>
            <td></td>
            <td>TemplateMatchingResults</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>vector_matching</td>
            <td></td>
            <td>VectorMatchingResults</td>
            <td>pyxem</td>
        </tr>
        <tr>
            <td>VirtualBSEImage</td>
            <td>virtual_backscatter_electron_image</td>
            <td>VirtualBSEImage</td>
            <td>kikuchipy</td>
        </tr>
        <tr>
            <td>virtual_dark_field</td>
            <td></td>
            <td>VirtualDarkFieldImage</td>
            <td>pyxem</td>
        </tr>
    </tbody>
</table>

##

