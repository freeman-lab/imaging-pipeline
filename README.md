# imaging-pipeline

> a pipeline for calcium imaging data built out of modular components

This is a small package for performing common steps in processing calcium imaging data. There's actually very little code here, because all the analyses are implemented in separate packages. This just wraps them with common arguments into something that can be run from the command line. So if this doesn't exactly match your needs, you might want to build your own version.

## install

For now, just clone this repository and run by calling

```
bin/imaging-pipeline
```

Once it's more fleshed out it will be installable using `pip`.

## commands

#### `registration -i /input -o /output -a crosscorr`

Perform image registration.

Options
- `-i` input data
- `-o` output location
- `-a` algorithm

#### `extraction -i /input -o /output -a nmf`

Perform source extraction.

Options
- `-i` input data
- `-o` output location
- `-a` algorithm

#### `visualization -i /input -o /output -ft detrend -fs median -dt 1 -ds 5`

Generate a movie to visualize raw data with optional filtering and downsampling.

Options
- `-i` input data
- `-o` output location
- `-ft` temporal filtering
- `-fs` spatial filtering
- `-dt` temporal downsampling
- `-ds` spatial downsampling

#### `regression -i /input -o /output -x covariates.json`

Perform pixel-wise linear regression.

Options
- `-i` input data
- `-o` output location
- `-x` covariates


