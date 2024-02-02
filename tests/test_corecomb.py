# Generated by CodiumAI

from corecomb import replace_ambiguous, write_xmfa


class TestReplaceAmbiguous:
    # Given a sequence containing only characters from the allowed alphabet, the function should return the same sequence.
    def test_same_sequence(self):
        seq = "ATCG"
        result = replace_ambiguous(seq)
        assert result == seq

    # Given a sequence containing ambiguous characters (not in the allowed alphabet), the function should replace them with Ns and return the cleaned sequence.
    def test_replace_ambiguous_characters(self):
        seq = "ATCGY"
        result = replace_ambiguous(seq)
        assert result == "ATCGN"

    # Given a sequence containing gaps (-), the function should return the same sequence.
    def test_same_sequence_with_gaps(self):
        seq = "ATCG-"
        result = replace_ambiguous(seq)
        assert result == seq

    # Given an empty sequence, the function should return an empty sequence.
    def test_empty_sequence(self):
        seq = ""
        result = replace_ambiguous(seq)
        assert result == ""

    # Given a sequence containing only ambiguous characters, the function should replace them all with Ns and return the cleaned sequence.
    def test_all_ambiguous_characters(self):
        seq = "RYMK"
        result = replace_ambiguous(seq)
        assert result == "NNNN"

    # Given a sequence containing only gaps (-), the function should return the same sequence.
    def test_same_sequence_with_only_gaps(self):
        seq = "-----"
        result = replace_ambiguous(seq)
        assert result == seq


# Generated by CodiumAI


class TestWriteXmfa:
    # writes XMFA file with correct gene order and genome sequences
    def test_correct_gene_order_and_genome_sequences(self, tmp_path):
        # Initialize test data
        seqdict = {
            "gene1": {"genome1": "ATCG", "genome2": "GCTA"},
            "gene2": {"genome1": "AAAA", "genome2": "TTTT"},
        }
        gene_order = ["gene1", "gene2"]
        genomes = ["genome1", "genome2"]
        gene_aln_len = {"gene1": 4, "gene2": 4}
        outfile = tmp_path / "test1.xmfa"

        # Invoke the function under test
        write_xmfa(seqdict, gene_order, genomes, gene_aln_len, outfile)

        # Read the generated XMFA file
        with open(outfile, "r") as f:
            xmfa_content = f.read()

        # Assert the XMFA file content is correct
        expected_xmfa_content = "# gene1\n>genome1:0-4\nATCG\n>genome2:0-4\nGCTA\n=\n# gene2\n>genome1:4-8\nAAAA\n>genome2:4-8\nTTTT\n=\n"
        assert xmfa_content == expected_xmfa_content

    # handles missing sequences for some genomes in a gene alignment
    def test_missing_sequences_for_some_genomes(self, tmp_path):
        # Initialize test data
        seqdict = {
            "gene1": {"genome1": "ATCG", "genome2": "GCTA"},
            "gene2": {"genome1": "AAAA"},
        }
        gene_order = ["gene1", "gene2"]
        genomes = ["genome1", "genome2"]
        gene_aln_len = {"gene1": 4, "gene2": 4}
        outfile = tmp_path / "test2.xmfa"

        # Invoke the function under test
        write_xmfa(seqdict, gene_order, genomes, gene_aln_len, outfile)

        # Read the generated XMFA file
        with open(outfile, "r") as f:
            xmfa_content = f.read()

        # Assert the XMFA file content is correct
        expected_xmfa_content = "# gene1\n>genome1:0-4\nATCG\n>genome2:0-4\nGCTA\n=\n# gene2\n>genome1:4-8\nAAAA\n>genome2\n----\n=\n"
        assert xmfa_content == expected_xmfa_content
