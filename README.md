# openvino_helper
easy save and load ccache, bin file

```sh
!pip install git+https://github.com/daehyun99/openvino_helper.git
```

### Easy Setting
```python
from openvino_helper.setting import setting

SETTING = setting(
    DRIVE_CACHE_ARCHIVE = "/content/drive/MyDrive/Build_Cache/[ccache_file_name].tar.gz",
    DRIVE_BIN_ARCHIVE = "/content/drive/MyDrive/Build_Cache/[ccache_bin_file_name].tar.gz",
    DRIVE_BUILD_ARCHIVE: str = "/content/drive/MyDrive/Build_Cache/build_openvino_TF_Front.tar.gz",
    LOCAL_CACHE_DIR = "/content/ccache_local",
    LOCAL_BIN_DIR = "content/openvino/bin"
    )
```

### Easy Load
```python
from openvino_helper.load import load

load(SETTING)
```

### Easy Save
```python
from openvino_helper.save import save

save(SETTING)
```
