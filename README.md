# cordex-esd-manager
The CORDEX-ESD experiment submissions manager Django project is being developed to support the Coordinate Regional Downscaling Downscaling Experiment (CORDEX) Empirical Statistical Downscaling (ESD) activity... phew!

The preliminary requirements are:
* To allow statistical downscaling experiments (though aiming for generic experiment description) in terms of experiment time periods, associated datasets, and required output.
* To allow experiment participants to submit results to an a particular experiment and have their results quality controlled, correctly annotated (meta-data added/corrected), and built/converted into standard data format (NetCDF) files named according to a defined Data Reference Syntax (DRS)

Current functionality covers the basics of requirement 1 and the file submission part of requirement 2.  The submission building/converting code is being developed separately though may be merged into this code at some point.

