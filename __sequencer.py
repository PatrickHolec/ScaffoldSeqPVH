
# libraries
import os,sys,shutil,time

class main:
    def __init__(self):
        self.anchor5 = 'ATATATATATATATATAT'
        self.anchor3 = 'TATATATATATATATATA'
        self.gstart = 'CGCGCGCGCGCGCGCGCG'
        self.gend = 'GCGCGCGCGCGCGCGCGC'
        self.dampening_power = 1
        self.similarity = 1
        self.indices = [i for i in xrange(5)]
        self.sample_count = 1000000
        self.filter_coeff = 1
        self.region_length = 13
        self.data_fnames = []
        
    def auto(self,prefix):
        # some user settings for sequences
        
        print 'Creating files...'
        
        for i in self.indices:
            data_fname = './sequences/{}_uniques_r{}.txt'.format(prefix,i)
            jobname = '{}_r{}'.format(prefix,i)
            job_fname = '{}_r{}.txt'.format(prefix,i)


            with open(job_fname,'w') as job:
                job.write("Job Name: {}\n".format(jobname))
                job.write("FASTA/FASTQ File: {}\n".format(data_fname))
                job.write("Gene Start: {}\n".format(self.gstart))
                job.write("5' Anchor: {}\n".format(self.anchor5))
                job.write("3' Anchor: {}\n".format(self.anchor3))
                job.write("# of Diversified Regions: 1\n")
                job.write("DNA After Region: {}\n".format(self.gend))
                job.write("Minimum Region Length: {}\n".format(self.region_length))
                job.write("Maximum Region Length: {}\n".format(self.region_length))
                job.write("Insert after # Position: 1\n")
                job.write("Sequence Similarity Threshold: {}\n".format(self.similarity))
                job.write("Frequency Dampening Power: {}\n".format(self.dampening_power))
                job.write("Maximum Sequence Count: {}\n".format(self.sample_count+1))
                job.write("Assay Background Filter: Off\n")
                job.write("Pairwise Analysis: On\n")
                job.write("Filter Coefficient: {}\n".format(self.filter_coeff))

            # Run scaffold seq using job instructions
            print 'Starting {} analysis...'.format(jobname)
            
            t0 = time.time()
            os.system('python __scaffoldseq.py {}'.format(job_fname))
            print ' --- {} seconds to execute ScaffoldSeq'.format(time.time()-t0)

            print 'Completed {}.'.format(jobname)

            # Clean up directories
            print 'Starting to clean directories...'

            rname = '{}_r{}'.format(prefix,i)
            suffix = ['_Region_1.csv','_Epistasis.csv','_Mutual-Information.csv']
            piclist = [f for f in os.listdir('./') if f.endswith('.png')]

            # move data files/pics
            for name in [rname+s for s in suffix]:
                shutil.move(name,'./scratch/'+name)
            for name in piclist:
                shutil.move(name,'./pics/'+name)
                
            # delete job txt
            os.remove(job_fname)

            print 'Completed cleaning.'
                
        print 'Finished!'

    def manual(self):

        print 'Starting manual scaffold sequence analysis...'
        for data_fname in self.data_fnames:

            jobname = os.path.splitext(data_fname)[0]
            job_fname = os.path.splitext(data_fname)[0] + '.txt'
            print 'Starting job {}...'.format(jobname)
                                              
            with open(job_fname,'w') as job:
                job.write("Job Name: {}\n".format(jobname))
                job.write("FASTA/FASTQ File: {}\n".format(data_fname))
                job.write("Gene Start: {}\n".format(self.gstart))
                job.write("5' Anchor: {}\n".format(self.anchor5))
                job.write("3' Anchor: {}\n".format(self.anchor3))
                job.write("# of Diversified Regions: 1\n")
                job.write("DNA After Region: {}\n".format(self.gend))
                job.write("Minimum Region Length: {}\n".format(self.region_length))
                job.write("Maximum Region Length: {}\n".format(self.region_length))
                job.write("Insert after # Position: 1\n")
                job.write("Sequence Similarity Threshold: {}\n".format(self.similarity))
                job.write("Frequency Dampening Power: {}\n".format(self.dampening_power))
                job.write("Maximum Sequence Count: {}\n".format(self.sample_count+1))
                job.write("Assay Background Filter: Off\n")
                job.write("Pairwise Analysis: On\n")
                job.write("Filter Coefficient: {}\n".format(self.filter_coeff))
    
            # Run scaffold seq using job instructions
            print 'Starting {} analysis...'.format(jobname)
            os.system('python __scaffoldseq.py {}'.format(job_fname))
            print 'Completed {}.'.format(jobname)

            # Clean up directories
            print 'Starting to clean directories...'

            suffix = ['_Region_1.csv','_Epistasis.csv','_Mutual-Information.csv']
            piclist = [f for f in os.listdir('./') if f.endswith('.png')]

            # move data files/pics
            for name in [jobname+s for s in suffix]:
                shutil.move(name,'./scratch/'+name)
            for name in piclist:
                shutil.move(name,'./pics/'+name)
                
            # delete job txt
            os.remove(job_fname)

            print 'Completed cleaning.'
                
        print 'Finished!'












