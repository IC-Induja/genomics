## script for comparing a baumanii genomes

## genome properties -> complete? percent coverage, species, accession.version
import GenomeSet from genomics
import prokka from companno
species = "A. baumanii"

genomes = GenomeSet.from_db(species="A. baumanii", complete_only=True, annotations_only=True)
## should immediately do entrez search and return : list of accessions, number of sequences,
## etc (non-sequence, non-annotation details)
annotation_tables = genomes.annotations

## AnnotationTableSet?? list of annotation tables?


genomes = GenomeSet.from_db(species="A. baumanii", complete_only=True, annotations=False)
annotated_genomes = prokka.annotate(genomes)

specimen = Sequence.from_file('species_file.fasta')
annotated_specimen = prokka.annotate(specimen)

companno.compare_against_reference(annotated_specimen, annotated_genomes, group_by="cogs")
                            #go also possible, if none is provided, will use gene name
# returns a dataframe of genes that are present/absent in other references, sorted by delta
