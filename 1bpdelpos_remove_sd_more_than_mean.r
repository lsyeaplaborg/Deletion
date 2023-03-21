setwd('/Volumes/HQ_data/delmap/1bpdelpos')

#work_dir='./'
#samples=c('HQ4661','HQ4662','HQ4663')
#ann_df=read.table('./HQ4661_A_filt_profile.txt',header = T)


cal_mean_sd=function(work_dir,ann_df,samples,out_file){
  df_all=data.frame()
  for (i in samples){
    f=read.table(file.path(work_dir,paste0(i,'_1bpdelpos_count.txt')),header = T,skip = 1)
    # remove count value
    f=f[(nrow(f)/2+1):nrow(f),]
    if (nrow(df_all)==0){
      df_all=f
    }else{
      df_all=merge(df_all,f,by = 'total_reads')
    }
  }
  
  df_all$Y=apply(df_all[,2:(1+length(samples))],1,function(x)mean(as.numeric(as.character(x))))
  df_all$sd=apply(df_all[,2:(1+length(samples))],1,function(x)sd(as.numeric(as.character(x))))
  df_all$Err=apply(df_all[,2:(1+length(samples))],1,function(x)sd(as.numeric(as.character(x)))/sqrt(length(samples)))
  
  # if mean
  idx=df_all$Y<df_all$sd
  df_all$Y[idx]=0
  df_all$Err[idx]=0
  
  df_all=merge(ann_df[,c(1,2)],df_all,by.x = 'Pos',by.y = 'total_reads')
  df_out=df_all[,c("Pos","Base","Y","Err")]
  
  write.table(df_out,out_file,quote = F,sep = '\t',row.names = F)
  
}


work_dir='/Volumes/HQ_data/delmap/1bpdelpos'
ann_df=read.table('/Users/haoqian/Downloads/tmp/HQ4661_A_filt_profile.txt',header = T)

samples=c('HQ4643','HQ4644','HQ4415','HQ4512','HQ4695','HQ4707','HQ4708','HQ4673','HQ4677','HQ4701','HQ4413','HQ4716','HQ4623','HQ4624','HQ4705','HQ4611','HQ4612','HQ4613','HQ4614','HQ4615','HQ4648','HQ4532','HQ4533','HQ4255','HQ4256','HQ4257')
cal_mean_sd(work_dir,ann_df,samples,out_file='./WT_1bpdelpos_filt_profile.txt')

samples=c('HQ4645','HQ4646','HQ4647')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Fen1_1bpdelpos_filt_profile.txt')

samples=c('HQ4416','HQ4513','HQ4514')
cal_mean_sd(work_dir,ann_df,samples,out_file='./UNG_1bpdelpos_filt_profile.txt')

samples=c('HQ4696','HQ4709','HQ4710','HQ4799')
cal_mean_sd(work_dir,ann_df,samples,out_file='./53BP1_1bpdelpos_filt_profile.txt')

samples=c('HQ4676','HQ4702','HQ4797','HQ4798')
cal_mean_sd(work_dir,ann_df,samples,out_file='./ATM_1bpdelpos_filt_profile.txt')

samples=c('HQ4951','HQ4641')
cal_mean_sd(work_dir,ann_df,samples,out_file='./H2AX_1bpdelpos_filt_profile.txt')

samples=c('HQ4414','HQ4711','HQ4800')
cal_mean_sd(work_dir,ann_df,samples,out_file='./XLF_1bpdelpos_filt_profile.txt')

samples=c('HQ4417','HQ4418','HQ4419','HQ4420')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Polh_1bpdelpos_filt_profile.txt')

samples=c('HQ4678','HQ4717','HQ4795')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Msh2_1bpdelpos_filt_profile.txt')

samples=c('HQ4680','HQ4699')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Msh2_UNG_He_1bpdelpos_filt_profile.txt')

samples=c('HQ4698')
cal_mean_sd(work_dir,ann_df,samples,out_file='./UM_1bpdelpos_filt_profile.txt')

samples=c('HQ4626','HQ4627','HQ4704','HQ4706')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Exo1_1bpdelpos_filt_profile.txt')

samples=c('HQ4617','HQ4619','HQ4620','HQ4621','HQ4622')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Pms2_1bpdelpos_filt_profile.txt')

samples=c('HQ4649','HQ4650','HQ4651','HQ4652')
cal_mean_sd(work_dir,ann_df,samples,out_file='./MLH1_1bpdelpos_filt_profile.txt')

samples=c('HQ4534','HQ4535','HQ4628')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Ape2_male_1bpdelpos_filt_profile.txt')

samples=c('HQ4713','HQ4714','HQ4715')
cal_mean_sd(work_dir,ann_df,samples,out_file='./Ape2_female_1bpdelpos_filt_profile.txt')

samples=c('HQ4258','HQ4259','HQ4260','HQ4261','HQ4262','HQ4263')
cal_mean_sd(work_dir,ann_df,samples,out_file='./AID_1bpdelpos_filt_profile.txt')