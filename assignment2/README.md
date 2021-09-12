
# README.md Assignment2

## Task 2.x

### Prerequisites

This code is bash code, it should be run under linux/WLS/Cywin environments.

### Functionality

Here you can name or list the functionalities your scripts
There are 2 functions, one is to move files, the other one is to track task time.

### Missing Functionality

Here you can name limitations.

### Usage

To move all files from source_dir to destination_dir the user needs to run the following command

```bash
move.sh source_dir destination_dir2
```

To move certain types of files from source_dir1 to destination_dir2 the user needs to run the following command

```bash
move.sh source_dir destination_dir2 file_extension
```

## Task 2.y

To track a task the user needs to run the following command

```bash
source trach.sh
track start task_label
```

To check the current task status the user needs to run the following command

```bash
track status
```

To stop the current tracking session the user needs to run the following command

```bash
track stop
```
