<p align="center">
    <img src="https://raw.githubusercontent.com/maxibor/corecomb/master/img/logo_text_small.png" width="300">
</p>

<p align="center">
    <a href="https://github.com/maxibor/corecomb/actions/workflows/ci.yaml">
        <img src="https://github.com/maxibor/corecomb/actions/workflows/ci.yaml/badge.svg" alt="Workflow status badge">
        <a href="https://pypi.org/project/corecomb"><img src="https://badge.fury.io/py/corecomb.svg" alt="PyPI version" height="18"></a>
    </a>
</p>

**Corecomb**: create a XMFA file from Panaroo core gene alignments to detect recombination in core-genome using ClonalFrameML.

## Installation

```bash
pip install corecomb
```

## Quick start

If you are in Panaroo output directory, just run: 

```
corerecomb 
```

## Get help

```bash
$ corecomb --help

 Usage: corecomb [OPTIONS]

 Create XMFA file from ClonalFrameML input from Panaroo core-genome gene alignments

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --gene_al_dir    TEXT  Path to directory containing core-genome gene alignments [default: core_gene_alignments]                 │
│ --pan_fa         TEXT  Path to Panaroo pan_genome_reference.fa [default: pan_genome_reference.fa]                               │
│ --extension      TEXT  File extension of core-genome gene alignments [default: fas]                                             │
│ --outfile        TEXT  Path to output XMFA file [default: corecomb.xmfa]                                                        │
│ --help                 Show this message and exit.                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Why

In theory, using the indivudal core-gene multiple sequence alignments from the `core_gene_alignments` directory of Panaroo, one could just run a `sed` command to concatenate these in a [XMFA file](https://darlinglab.org/mauve/user-guide/files.html).

```bash
sed -e '$s/$/\n=/' -s ../tests/data/aligned_gene_sequences_raw/*.fas > core_gene_alignment.xmfa
```

However, this approach suffers from 3 different issues:

- Sequence names need to be cleaned
- Ambiguous non `N` IUPAC characters need to be taken care of (CFML only accepts `A,T,G,C,N,-`)
- Genomes with missing genes will cause CFML to crash (core-genome defined at less 100%)

> CoRecomb addresses all 3 of these issues. Additionally, CoRecomb uses the order of the genes [defined in the `pan_genome_reference.fa`](https://github.com/gtonkinhill/panaroo/issues/146) to re-order the genes in the XMFA file (which will be kept by CFML output `core_gene_test_cfml.filtered.fasta`).

## Test it for yourself

```bash
poetry run pytest -vv
```

Test data can be found here [tests/data](tests/data)

```bash
corecomb \
    --gene_al_dir tests/data/aligned_gene_sequences_raw \
    --pan_fa tests/data/pan_genome_reference.fa \
    --extension fas \
    --outfile corecomb.xmfa
```

## Use the XMFA with ClonalFrameML

```bash
ClonalFrameML \
    input_tree.nwk \
    corecomb.xmfa \
    cfml_output_basename \
    -xmfa_file true \
    -show_progress true \
    -output_filtered true
```
