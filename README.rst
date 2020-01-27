Flicker Noise Formulations in Compact Models
============================================

Includes a resistor model that demonstrates how to properly model flicker noise 
in Verilog-A as described in "Flicker Noise Formulations in Compact Models", to 
be published in Transactions on Computer-Aided Design of Integrated Circuits and
Systems some time in 2020.

Also included are two circuits. The first is a simple test circuit for the 
resistor model. The second is a circuit that tests the implementation of flicker 
noise in the built-in BSIM4 model.

If you have a recent version of Spectre, you can simulate the circuits directly 
and view the results in your favorite waveform viewer.

If you have Python 3.6 or later, you can also run the simulation scripts, which
re-generate the netlists, run the simulation (in Spectre), and plot the results.

To install the script dependencies, from the directory that contains setup.py,
run::

   pip3 install --user .

This installs all dependencies into ~/.local/lib.  Then simply run::

   ./runPnoise

or::

   ./runBSIM

These run a simulation and plot the results. You have the -v option and the 
logfile (.runPnoise.log or .runBSIM.log) to help you out if you run into any 
problems.

You can also run a simulation of the broken resistor model::

  ./runPnoise --broken

You can view the signal and waveforms with::

   > list-psf -f pnoise.raw/pnoise.pnoise -l
   > plot-psf out

My rather old version of Spectre (15.1.0) generated the following results:

Resistor:

    .. image:: figures/resistor.svg

BSIM:

    .. image:: figures/bsim.svg
