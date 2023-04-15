# CREAM 
The repo of ICSE 2023 paper "Two Sides of the Same Coin: Exploiting the Impact of Identifiers in Neural Code Comprehension". This repo contains the code of our framework on all tasks. We propose a framework to improve the robustness and accuracy of neural code models. It is flexible and can be used on any neural code models. You can try it on your own model :).

## Function Naming
Function naming aims to automatically generate a meaningful and succinct name for a function. We use the widely used CodeSearchNet (CSN) dataset which contains six programming languages including Java, Python, Go, PHP, JavaScript and Ruby.
- Data source: https://drive.google.com/uc?id=1rd2Tc6oUWBo7JouwexW3ksQ0PaOhUr6h

Train and inference
```bash
cd function naming
bash name.sh
bash name_test.sh
```

## Defect Detection
Defect detection aims to identify whether a given code snippet is vulnerable. We use the defect detection dataset released by Devign. The dataset contains 27,318 C code snippets collected from the QEMU and FFmpeg projects.
- Data source: https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Defect-detection

Train and inference
```bash
cd defect detection
bash finetune.sh
bash inference.sh
```

## Code Classification
Code classification is the task of classifying a code snippet by its functionality. For code classification, we use the POJ dataset which contains 52,000 code snippets of C language with 104 classes. It is collected from Online Judge (OJ) and code snippets in the same class are used to solve the same programming problem.
- Data source: https://github.com/zhangj111/astnn/tree/master/data

Train and inference
```bash
cd code classfication
bash cfinetune.sh
bash cinference.sh
```


# Full Results of Function Naming
## Java
| Approach | Original Precision | Original Recall | Original F1 | Transformed Precision | Transformed Recall | Transformed F1 |
|----------|--------------------|-----------------|-------------|-----------------------|--------------------|----------------|
| CodeNN   | 38.24              | 31.76           | 33.18       | 27.33                 | 21.99              | 23.05          |
| +CREAM   | 39.59              | 31.96           | 33.69       | 35.47                 | 25.98              | 28.35          |
| NCS      | 38.86              | 34.46           | 35.07       | 24.15                 | 21.34              | 21.61          |
| +CREAM   | 38.99              | 35.46           | 35.63       | 30.21                 | 27.00              | 27.28          |
| CodeBERT | 49.24              | 46.72           | 46.38       | 26.45                 | 27.90              | 25.90          |
| +CREAM   | 50.40              | 47.01           | 47.04       | 39.65                 | 36.96              | 36.72          |


## Python
| Approach | Original Precision | Original Recall | Original F1 | Transformed Precision | Transformed Recall | Transformed F1 |
|----------|--------------------|-----------------|-------------|-----------------------|--------------------|----------------|
| CodeNN   | 26.61              | 21.57           | 22.64       | 4.41                  | 3.96               | 4.00           |
| +CREAM   | 27.16              | 21.41           | 22.69       | 6.68                  | 5.03               | 5.44           |
| NCS      | 30.53              | 24.10           | 25.68       | 4.23                  | 3.51               | 3.65           |
| +CREAM   | 29.09              | 24.59           | 25.40       | 5.23                  | 4.70               | 4.67           |
| CodeBERT | 40.30              | 37.69           | 37.64       | 4.95                  | 5.76               | 5.05           |
| +CREAM   | 40.69              | 37.48           | 37.66       | 7.64                  | 7.76               | 7.29           |

## JavaScript
| Approach | Original Precision | Original Recall | Original F1 | Transformed Precision | Transformed Recall | Transformed F1 |
|----------|--------------------|-----------------|-------------|-----------------------|--------------------|----------------|
| CodeNN   | 17.11              | 13.77           | 14.40       | 5.46                  | 4.74               | 4.72           |
| +CREAM   | 16.91              | 13.60           | 14.16       | 8.10                  | 5.51               | 6.00           |
| NCS      | 19.10              | 15.53           | 16.31       | 3.96                  | 3.21               | 3.22           |
| +CREAM   | 20.37              | 15.39           | 16.46       | 9.33                  | 6.64               | 7.20           |
| CodeBERT | 31.77              | 29.47           | 29.55       | 4.81                  | 4.98               | 4.61           |
| +CREAM   | 31.50              | 25.52           | 27.11       | 11.89                 | 10.43              | 10.54          |

## PHP
| Approach | Original Precision | Original Recall | Original F1 | Transformed Precision | Transformed Recall | Transformed F1 |
|----------|--------------------|-----------------|-------------|-----------------------|--------------------|----------------|
| CodeNN   | 42.14              | 35.59           | 36.83       | 19.67                 | 17.96              | 17.61          |
| +CREAM   | 42.35              | 35.56           | 36.87       | 27.43                 | 21.01              | 22.44          |
| NCS      | 44.50              | 39.35           | 40.19       | 18.70                 | 18.15              | 17.56          |
| +CREAM   | 43.34              | 40.53           | 40.25       | 25.58                 | 25.32              | 24.38          |
| CodeBERT | 51.92              | 49.75           | 49.36       | 22.25                 | 27.38              | 23.43          |
| +CREAM   | 53.37              | 20.37           | 50.35       | 36.53                 | 37.85              | 35.80          |

## Go
| Approach | Original Precision | Original Recall | Original F1 | Transformed Precision | Transformed Recall | Transformed F1 |
|----------|--------------------|-----------------|-------------|-----------------------|--------------------|----------------|
| CodeNN   | 39.10              | 34.01           | 34.64       | 20.61                 | 17.58              | 17.79          |
| +CREAM   | 39.92              | 33.82           | 34.79       | 29.20                 | 24.01              | 24.91          |
| NCS      | 42.92              | 41.50           | 40.52       | 22.29                 | 23.35              | 21.68          |
| +CREAM   | 41.79              | 42.08           | 40.21       | 28.60                 | 28.63              | 27.33          |
| CodeBERT | 53.19              | 50.06           | 49.88       | 28.16                 | 30.14              | 27.72          |
| +CREAM   | 52.96              | 50.81           | 50.28       | 39.85                 | 40.57              | 38.62          |

## Ruby
| Approach | Original Precision | Original Recall | Original F1 | Transformed Precision | Transformed Recall | Transformed F1 |
|----------|--------------------|-----------------|-------------|-----------------------|--------------------|----------------|
| CodeNN   | 15.28              | 11.32           | 12.24       | 7.69                  | 5.40               | 5.98           |
| +CREAM   | 15.05              | 11.63           | 12.36       | 9.66                  | 6.36               | 7.25           |
| NCS      | 13.80              | 13.80           | 12.93       | 6.23                  | 5.98               | 5.70           |
| +CREAM   | 16.18              | 13.15           | 13.64       | 12.58                 | 9.93               | 10.47          |
| CodeBERT | 34.16              | 32.42           | 32.04       | 21.24                 | 22.24              | 20.72          |
| +CREAM   | 32.79              | 30.96           | 30.49       | 29.57                 | 28.05              | 27.49          |


# Full Results of parameter analysis on CodeBERT
## Function naming Java
| alpha | Original F1 | Transformed F1 |
|-------|-------------|----------------|
| 0     | 46.00       | 30.61          |
| 0.1   | 46.32       | 32.58          |
| 0.2   | 46.41       | 33.49          |
| 0.3   | 46.55       | 34.41          |
| 0.4   | 46.99       | 35.37          |
| 0.5   | 47.04       | 35.98          |
| 0.6   | 47.04       | 36.72          |
| 0.7   | 46.96       | 37.39          |
| 0.8   | 46.47       | 37.44          |
| 0.9   | 46.23       | 38.03          |
| 1     | 46.06       | 38.67          |

| I_{fusion} | Original F1 | Transformed F1 |
|------------|-------------|----------------|
| 0          | 46.84       | 34.48          |
| 0.1        | 47.04       | 36.72          |
| 0.2        | 47.81       | 36.72          |
| 0.3        | 48.01       | 36.63          |


## Function naming Python
| alpha | Original F1 | Transformed F1 |
|-------|-------------|----------------|
| 0     | 37.34       | 6.73           |
| 0.1   | 37.52       | 7.00           |
| 0.2   | 37.36       | 7.19           |
| 0.3   | 37.56       | 7.31           |
| 0.4   | 37.66       | 7.29           |
| 0.5   | 37.53       | 7.86           |
| 0.6   | 37.24       | 8.42           |
| 0.7   | 37.46       | 8.75           |
| 0.8   | 37.00       | 9.38           |
| 0.9   | 36.68       | 9.70           |
| 1     | 36.36       | 9.99           |

| I_{fusion} | Original F1 | Transformed F1 |
|------------|-------------|----------------|
| 0          | 37.07       | 7.12           |
| 0.1        | 37.66       | 7.29           |
| 0.2        | 37.30       | 8.01           |
| 0.3        | 37.75       | 8.13           |

## Function naming PHP
| alpha | Original F1 | Transformed F1 |
|-------|-------------|----------------|
| 0     | 50.11       | 31.64          |
| 0.1   | 50.29       | 32.92          |
| 0.2   | 50.37       | 34.14          |
| 0.3   | 50.40       | 35.39          |
| 0.4   | 50.35       | 35.80          |
| 0.5   | 50.34       | 37.55          |
| 0.6   | 50.29       | 38.44          |
| 0.7   | 50.15       | 39.35          |
| 0.8   | 49.86       | 40.19          |
| 0.9   | 49.66       | 40.89          |
| 1     | 49.33       | 41.56          |

| I_{fusion} | Original F1 | Transformed F1 |
|------------|-------------|----------------|
| 0          | 50.22       | 35.67          |
| 0.1        | 50.35       | 35.80          |
| 0.2        | 50.23       | 35.66          |
| 0.3        | 50.08       | 36.15          |

## Function naming JS
| alpha | Original F1 | Transformed F1 |
|-------|-------------|----------------|
| 0     | 26.79       | 7.93           |
| 0.1   | 26.81       | 8.30           |
| 0.2   | 26.94       | 8.86           |
| 0.3   | 27.21       | 9.78           |
| 0.4   | 27.10       | 10.25          |
| 0.5   | 27.11       | 10.54          |
| 0.6   | 26.69       | 10.50          |
| 0.7   | 26.22       | 10.82          |
| 0.8   | 25.81       | 10.93          |
| 0.9   | 24.88       | 11.45          |
| 1     | 24.56       | 12.16          |

| I_{fusion} | Original F1 | Transformed F1 |
|------------|-------------|----------------|
| 0          | 26.99       | 9.89           |
| 0.1        | 27.11       | 10.54          |
| 0.2        | 26.58       | 10.24          |
| 0.3        | 26.48       | 9.74           |

## Function naming Ruby
| alpha | Original F1 | Transformed F1 |
|-------|-------------|----------------|
| 0     | 28.64       | 19.34          |
| 0.1   | 29.24       | 20.20          |
| 0.2   | 29.42       | 21.14          |
| 0.3   | 29.29       | 22.44          |
| 0.4   | 29.54       | 22.47          |
| 0.5   | 29.86       | 23.63          |
| 0.6   | 30.31       | 24.65          |
| 0.7   | 30.47       | 26.32          |
| 0.8   | 30.49       | 27.49          |
| 0.9   | 30.35       | 27.35          |
| 1     | 30.06       | 27.93          |

| I_{fusion} | Original F1 | Transformed F1 |
|------------|-------------|----------------|
| 0          | 30.36       | 26.16          |
| 0.1        | 30.49       | 27.49          |
| 0.2        | 29.12       | 27.45          |
| 0.3        | 29.21       | 27.34          |


## Function naming Go
| alpha | Original F1 | Transformed F1 |
|-------|-------------|----------------|
| 0     | 49.48       | 33.30          |
| 0.1   | 49.59       | 34.30          |
| 0.2   | 49.79       | 35.30          |
| 0.3   | 50.01       | 36.30          |
| 0.4   | 50.11       | 37.00          |
| 0.5   | 50.28       | 37.73          |
| 0.6   | 50.28       | 38.62          |
| 0.7   | 50.01       | 39.41          |
| 0.8   | 50.03       | 40.16          |
| 0.9   | 49.72       | 40.91          |
| 1     | 49.57       | 41.49          |

| I_{fusion} | Original F1 | Transformed F1 |
|------------|-------------|----------------|
| 0          | 49.85       | 37.73          |
| 0.1        | 50.28       | 38.62          |
| 0.2        | 49.96       | 38.51          |
| 0.3        | 49.75       | 38.91          |


## Defect detection
| alpha | Original ACC | Transformed ACC |
|-------|-------------|----------------|
| 0     | 63.54       | 59.37          |
| 0.1   | 63.95       | 59.69          |
| 0.2   | 64.05       | 60.25          |
| 0.3   | 63.95       | 60.76          |
| 0.4   | 64.27       | 61.02          |
| 0.5   | 64.09       | 61.31          |
| 0.6   | 64.05       | 62.01          |
| 0.7   | 63.95       | 61.97          |
| 0.8   | 63.84       | 62.04          |
| 0.9   | 63.76       | 62.19          |
| 1     | 63.65       | 62.23          |

| I_{fusion} | Original ACC | Transformed ACC |
|------------|-------------|----------------|
| 0          | 63.54       | 61.93          |
| 0.1        | 64.05       | 62.01          |
| 0.2        | 64.09       | 62.16          |
| 0.3        | 64.20       | 62.04          |


## Code classification
| alpha | Original ACC | Transformed ACC |
|-------|-------------|----------------|
| 0     | 98.08       | 95.21          |
| 0.1   | 98.17       | 97.54          |
| 0.2   | 98.2        | 97.48          |
| 0.3   | 98.23       | 97.52          |
| 0.4   | 98.24       | 97.55          |
| 0.5   | 98.25       | 97.57          |
| 0.6   | 98.28       | 97.59          |
| 0.7   | 98.22       | 97.63          |
| 0.8   | 98.15       | 97.66          |
| 0.9   | 98.11       | 97.67          |
| 1     | 98.08       | 97.68          |

| I_{fusion} | Original ACC | Transformed ACC |
|------------|-------------|----------------|
| 0          | 98.36       | 97.91          |
| 0.1        | 98.28       | 97.59          |
| 0.2        | 98.28       | 97.63          |
| 0.3        | 98.26       | 97.73          |
