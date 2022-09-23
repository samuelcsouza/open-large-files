# Open Large Files with Python

A brief example of how to read just a few lines from a large file without loading it entirely into your computer's memory.

The dataset has been provided by [Kaggle](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data)

## Functions

### read_file

The function receives three params:

- **file_path**: the path to the file;
- **skip**: number of lines you want to skip;
- **limit**: max number of lines you get;

This function returns a *Iterable* Object, you need to append all values into a list. In the *main.py* file you found a minimal example of how it works.

```python
lines_of_interest = read_file(
    file_path="./data/DailyDelhiClimateTrain.csv",
    skip=0,
    limit=100
)
```
