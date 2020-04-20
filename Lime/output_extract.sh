#!/usr/bin/env bash

stage=1
if [ $stage -le 0 ]; then
  for model in LoResNet10 ; do
    python Lime/output_extract.py \
      --model ${model} \
      --epochs 19 \
      --train-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/Vox1_spect/dev \
      --test-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/Vox1_spect/test \
      --sitw-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/sitw \
      --check-path /home/yangwenhao/local/project/DeepSpeaker-pytorch/Data/checkpoint/LoResNet10/spect/soft \
      --extract-path Lime/${model} \
      --dropout-p 0.5 \
      --sample-utt 500

  done
fi

if [ $stage -le 1 ]; then
#  for model in LoResNet10 ; do
#  python Lime/output_extract.py \
#    --model LoResNet10 \
#    --start-epochs 36 \
#    --epochs 36 \
#    --train-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/Vox1_spect/dev \
#    --test-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/Vox1_spect/test \
#    --sitw-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/sitw \
#    --loss-type center \
#    --check-path /home/yangwenhao/local/project/DeepSpeaker-pytorch/Data/checkpoint/LoResNet10/spect_cmvn/center_dp25 \
#    --extract-path Data/gradient \
#    --dropout-p 0 \
#    --gpu-id 0 \
#    --embedding-size 1024 \
#    --sample-utt 2000

  python Lime/output_extract.py \
    --model LoResNet10 \
    --start-epochs 24 \
    --epochs 24 \
    --train-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/Vox1_spect/dev \
    --test-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/Vox1_spect/test \
    --sitw-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/sitw \
    --loss-type soft \
    --check-path /home/yangwenhao/local/project/DeepSpeaker-pytorch/Data/checkpoint/LoResNet10/spect_cmvn/soft_dp25 \
    --extract-path Data/gradient \
    --dropout-p 0 \
    --gpu-id 0 \
    --embedding-size 1024 \
    --sample-utt 2000
#  done
fi
stage=3

if [ $stage -le 2 ]; then
  model=LoResNet10
  dataset=timit
  feat=spect_161
  loss=soft

  python Lime/output_extract.py \
    --model LoResNet10 \
    --train-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/timit/train_spect_noc \
    --test-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/timit/test_spect_noc \
    --start-epochs 15 \
    --check-path Data/checkpoint/LoResNet10/timit_spect/soft_var \
    --epochs 15 \
    --sitw-dir /home/yangwenhao/local/project/lstm_speaker_verification/data/sitw \
    --sample-utt 1500 \
    --embedding-size 128 \
    --extract-path Data/gradient/${model}/${dataset}/${feat}/${loss}_var_1500 \
    --model ${model} \
    --channels 4,16,64 \
    --dropout-p 0.0 \
    --epoch 20
fi
