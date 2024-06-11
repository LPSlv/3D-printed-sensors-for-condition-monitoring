# 3D Printed Sensors for Electric Motor Condition Monitoring

## Overview

This project focuses on developing a method for using 3D printed electrically conductive material sensors to monitor the condition of an electric motor. The study yielded 40 datasets containing time series data of deformations caused by vibrations in 10 different electric motors. Three conditions were monitored:
1. Worn or new motor
2. Cracked or intact motor mount
3. Wheel attached or detached from the motor shaft

Features were extracted from the signals using power spectral density and used for classification with the Random Forest method. The results showed feature separation between used and unused motor conditions, achieving 79% accuracy and 88% recall.

## Key Metrics

| Class                  | Accuracy | Precision | Recall | F1 Score |
|------------------------|----------|-----------|--------|----------|
| Worn Motor             | 0.788    | 0.817     | 0.875  | 0.804    |
| Cracked Mount          | 0.688    | 0.667     | 0.542  | 0.567    |
| Wheel Attached         | 0.513    | 0.467     | 0.667  | 0.542    |

## Sensor Design

Based on the literature review, a 3D printed resistance sensor was developed using Proto-pasta's electrically conductive material. The sensor specifications are:
- Active part length: 12 mm
- Thickness: 0.6 mm
- Trace width: 1.6 mm
- Base thickness: 0.1 mm
- Unstressed resistance: ~4.2 kΩ
- Theoretical maximum measurement frequency: 13.6 kHz

## Data Collection

An Arduino Leonardo and a voltage divider circuit were used for data collection.

## Experimentation

Using the developed 3D printed sensor, data collection circuit, and Pololu micro metal gearmotors with controllers, measurements of deformations caused by motor vibrations were conducted. The obtained datasets consisted of at least 60-second long time series data for various motor condition combinations: worn motor, cracked motor mount, and attached wheel.

## Classification

To test the applicability of the developed sensor and measurement scheme for condition monitoring, a Random Forest classification was performed using power spectral density for feature extraction. The analysis indicated feature separation for the worn motor class, while other classes showed overlap. The classification metrics are summarized in the table above, with the worn motor class showing the highest performance.

## Conclusion

The developed 3D printed sensor and measurement scheme can be used to determine motor wear. The high recall metric indicates potential applications in scenarios where failure to detect motor damage could lead to significant system damage or safety risks. 

## Future Work

Further research is needed to:
1. Improve the reliability of 3D printed sensor results to reduce the number of invalid datasets, such as enhancing the electrical connections between the sensor and measurement scheme.
2. Explore other feature extraction methods and algorithms to improve classification for other conditions. This could include calculating additional features or using other machine learning algorithms.
