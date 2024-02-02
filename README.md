<p align="center">
    <img src="img/logo_text.png" width="300">
</p>

<p align="center">
    <a href="https://github.com/maxibor/corecomb/actions/workflows/ci.yaml">
        <img src="https://github.com/maxibor/corecomb/actions/workflows/ci.yaml/badge.svg" alt="Workflow status badge">
    </a>
</p>

**CoRecomb**: create a XMFA file from Panaroo core gene alignments to detect recombination in core-genome using ClonalFrameML

# Installation

```bash
pip install corecomb
```

# Quick start

If you are in Panaroo output directory, just run: 

```
corerecomb 
```

# Get help

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

# Test it for yourself

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
