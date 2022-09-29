import argparse
import sys

def checkm_parse(input_path,output_path):
    with open(output_path,'w') as OutFile:
        with open(input_path,'r') as InFile:
            next(InFile)
            lines = InFile.readlines()
            for line in lines:
                line = line.strip()
                genome = line.split('\t')[0]
                lineage = line.split('\t')[1]
                completeness = line.split('\t')[11]
                contamination = line.split('\t')[12]
                if float(completeness) >= 50 and float(contamination) <= 10:
                    print(str(genome)+'\t'+str(lineage)+'\t'+str(completeness)+'\t'+str(contamination),file=OutFile)
        InFile.close()
    OutFile.close()

def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Checkm filter completeness>=50 and contamination<=10')
    parser.add_argument("-i", "--input",help="directionary to your input e.g. /home/bins_qa.txt")
    parser.add_argument("-o", "--output",help="directionary to your input e.g. /home/bins_qa.filter.txt")
    print(parser.parse_args(argv))
    return parser.parse_args(argv)

def main(arg):
    input_path=arg.input
    print(input_path)
    output_path=arg.output
    checkm_parse(input_path,output_path)

if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))