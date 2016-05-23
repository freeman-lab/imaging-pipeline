# imaging-pipeline

> a pipeline for calcium imaging data built out of modular components

This is a small tool for performing commong steps in processing calcium imaging data. There's very little code here, with the core analyses being implemented in separate packages. So if it doesn't exactly match your needs

# commands

#### `imaging-pipeline registration -i /input -o /output -a crosscorr`

Perform image registration.

Options
- `-i` input data
- `-o` output data
- `-a` algorithm

#### `imaging-pipeline movie -i /input -o /output -dt 1 -ds 5`

Generate a movie with filtering and downsampling.

Options
- `-i` input data
- `-o` output data
- `-dt` temporal downsampling
- `-ds` spatial downsampling

#### `imaging-pipeline regression -i /input -o /output -x covariates.json`

Perform pixel-wise linear regression.

Options
- `-i` input data
- `-o` output data
- `-x` covariates


