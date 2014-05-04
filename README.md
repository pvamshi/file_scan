#### File Scanner 

Scans the spcified folder path (or the current path ) for folders and subfolders and returns a json array with files and folders structure. 


For example: 

A test file structure is provided which contains the folder structure as follows : 

 test_files
    |-- dir1
    |   |-- dir11
    |   |   |-- file111.txt
    |   |   `-- file112.txt
    |   |-- dir12
    |   |-- file11.txt
    |   |-- file12.txt
    |   |-- file13.txt
    |   `-- file14.txt
    |-- dir2
    |   |-- dir21
    |   |-- dir22
    |   |   |-- 221
    |   |   `-- file221.txt
    |   `-- file21.txt
    |-- file1.txt
    |-- file2.txt
    `-- file3.txt

The json output generated for this is as follows :

```json
[
    {
        "name": "test_files",
        "path": "/home/vamshi/projects/file_scan/test_files",
        "isdir": true,
        "parent_file": "0",
        "children_dirs": [
            3,
            12
        ],
        "children_files": [
            1,
            2,
            18
        ]
    },
    {
        "name": "file1.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/file1.txt",
        "isdir": false,
        "parent_file": "0",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "file3.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/file3.txt",
        "isdir": false,
        "parent_file": "0",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "dir1",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1",
        "isdir": true,
        "parent_file": "0",
        "children_dirs": [
            5,
            10
        ],
        "children_files": [
            4,
            8,
            9,
            11
        ]
    },
    {
        "name": "file14.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/file14.txt",
        "isdir": false,
        "parent_file": "3",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "dir11",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/dir11",
        "isdir": true,
        "parent_file": "3",
        "children_dirs": [],
        "children_files": [
            6,
            7
        ]
    },
    {
        "name": "file112.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/dir11/file112.txt",
        "isdir": false,
        "parent_file": "5",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "file111.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/dir11/file111.txt",
        "isdir": false,
        "parent_file": "5",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "file11.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/file11.txt",
        "isdir": false,
        "parent_file": "3",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "file12.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/file12.txt",
        "isdir": false,
        "parent_file": "3",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "dir12",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/dir12",
        "isdir": true,
        "parent_file": "3",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "file13.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir1/file13.txt",
        "isdir": false,
        "parent_file": "3",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "dir2",
        "path": "/home/vamshi/projects/file_scan/test_files/dir2",
        "isdir": true,
        "parent_file": "0",
        "children_dirs": [
            14,
            15
        ],
        "children_files": [
            13
        ]
    },
    {
        "name": "file21.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir2/file21.txt",
        "isdir": false,
        "parent_file": "12",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "dir21",
        "path": "/home/vamshi/projects/file_scan/test_files/dir2/dir21",
        "isdir": true,
        "parent_file": "12",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "dir22",
        "path": "/home/vamshi/projects/file_scan/test_files/dir2/dir22",
        "isdir": true,
        "parent_file": "12",
        "children_dirs": [
            17
        ],
        "children_files": [
            16
        ]
    },
    {
        "name": "file221.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/dir2/dir22/file221.txt",
        "isdir": false,
        "parent_file": "15",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "221",
        "path": "/home/vamshi/projects/file_scan/test_files/dir2/dir22/221",
        "isdir": true,
        "parent_file": "15",
        "children_dirs": [],
        "children_files": []
    },
    {
        "name": "file2.txt",
        "path": "/home/vamshi/projects/file_scan/test_files/file2.txt",
        "isdir": false,
        "parent_file": "0",
        "children_dirs": [],
        "children_files": []
    }
]
