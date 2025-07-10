# Pipelining AI/ML Training Workloads with CUDA Streams

*Published on Towards Data Science, June 26, 2025*  
*By Chaim Rand*

## Overview

This article explores how to use CUDA streams in PyTorch to pipeline AI/ML training workloads, allowing different parts of the computation graph to run concurrently on the GPU. This can improve throughput and GPU utilization, especially when the model can be split into subgraphs (e.g., a frozen encoder and a trainable decoder) or when data preprocessing is offloaded to the GPU.

---

## 1. Pipelining an Encoder-Decoder Model

### Scenario

- A CNN-based image segmentation model with a **frozen encoder** and a **trainable decoder**.
- The encoder is run with `torch.no_grad()`, and only the decoder is trained.

### Baseline Training Loop

```python
for idx, data in enumerate(train_loader):
    inputs = data[0].to(device=device, non_blocking=True).float()
    labels = data[1].to(device=device, non_blocking=True)
    optimizer.zero_grad()
    with torch.no_grad():
        features = encoder(inputs)
    output = decoder(features)
    loss = criterion(output, labels)
    loss.backward()
    optimizer.step()
```

- **Result:** Average throughput of 83 steps/sec, GPU utilization 85%.

### Pipelined Training Loop with CUDA Streams

```python
encoder_stream = torch.cuda.Stream()
decoder_stream = torch.cuda.Stream()
features = None

for idx, data in enumerate(train_loader):
    inputs = data[0].to(device, non_blocking=True).float()
    labels_next = data[1].to(device, non_blocking=True)

    if features is not None:
        with torch.cuda.stream(decoder_stream):
            decoder_stream.wait_stream(encoder_stream)
            optimizer.zero_grad()
            output = decoder(features)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()

    with torch.cuda.stream(encoder_stream):
        with torch.no_grad():
            features = encoder(inputs)
        features.record_stream(encoder_stream)

    labels = labels_next
    # ...timing and break logic...
```

- **Result:** Throughput increases to 91 steps/sec (~9.6% speedup).

---

## 2. Pipelining Data Augmentation

### Scenario

- Data augmentations are performed on the GPU using custom transforms.
- Augmentations and model training are done sequentially in the baseline.

### Baseline Augmentation and Training

```python
for idx, data in enumerate(train_loader):
    inputs = data[0].to(device=device, non_blocking=True)
    labels = data[1].to(device=device, non_blocking=True).squeeze()
    inputs = batch_transform(inputs)
    optimizer.zero_grad()
    output = model(inputs)
    loss = criterion(output, labels)
    loss.backward()
    optimizer.step()
```

- **Result:** Throughput of 35.22 steps/sec (72.57% speedup over original baseline).

### Pipelined Augmentation and Training with CUDA Streams

```python
transform_stream = torch.cuda.Stream()
model_stream = torch.cuda.Stream()
transformed = None

for idx, data in enumerate(train_loader):
    inputs = data[0]
    labels_next = data[1]

    if transformed is not None:
        with torch.cuda.stream(model_stream):
            labels = labels.to(device, non_blocking=True).squeeze()
            model_stream.wait_stream(transform_stream)
            optimizer.zero_grad()
            output = model(transformed)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()

    with torch.cuda.stream(transform_stream):
        inputs = inputs.to(device, non_blocking=True)
        transformed = batch_transform(inputs)
        transformed.record_stream(transform_stream)

    labels = labels_next
    # ...timing and break logic...
```

- **Result:** Throughput increases to 38.82 steps/sec (~10.2% speedup over serialized solution, 90.2% faster than original baseline).

---

## Key Takeaways

- Pipelining with CUDA streams can improve throughput, especially when the GPU is underutilized.
- The benefit depends on the workload; if one part dominates runtime, pipelining may not help.
- Always profile and test on your own workloads before adopting this technique.

---

For more details, code, and performance analysis, see the full article:  
[Pipelining AI/ML Training Workloads with CUDA Streams](https://towardsdatascience.com/pipelining-ai-ml-training-workloads-with-cuda-streams/) 