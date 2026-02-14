import os
import subprocess

def load(SETTING):
    DRIVE_CACHE_ARCHIVE = SETTING["DRIVE_CACHE_ARCHIVE"]
    DRIVE_BIN_ARCHIVE = SETTING["DRIVE_BIN_ARCHIVE"]
    DRIVE_BUILD_ARCHIVE = SETTING["DRIVE_BUILD_ARCHIVE"]
    LOCAL_BUILD_DIR = SETTING["LOCAL_BUILD_DIR"]
    
    if os.path.exists(DRIVE_CACHE_ARCHIVE):
        print("📥 [CCACHE] 구글 드라이브에서 캐시를 가져오는 중...")
        try:
            subprocess.run(["tar", "-xzf", DRIVE_CACHE_ARCHIVE, "-C", "/"], check=True)
            print("✅ [CCACHE] 복원 완료!")
        except:
            print("❌ [CCACHE] tar 압축 해제 과정에서 에러가 발생했습니다.")
    else:
        print("ℹ️ [CCACHE] 저장된 캐시가 없습니다. 다시 빌드해야 합니다.")

    if os.path.exists(DRIVE_BIN_ARCHIVE):
        print("📥 [BIN] 구글 드라이브에서 실행 파일(bin)을 가져오는 중...")
        try:
            subprocess.run(["rm", "-rf", "/content/openvino/bin"], check=True)
            os.makedirs("/content/openvino", exist_ok=True)
            subprocess.run(["tar", "-xzf", DRIVE_BIN_ARCHIVE, "-C", "/content/openvino"], check=True)
            print("✅ [BIN] 복원 완료!")
        except:
            print("❌ [BIN] 실행 파일 복원 및 압축 해제 과정에서 에러가 발생했습니다.")
    else:
        print("ℹ️ [BIN] 저장된 실행 파일이 없습니다. 다시 빌드해야 합니다.")

    if os.path.exists(DRIVE_BUILD_ARCHIVE):
        print("📥 [BUILD] 구글 드라이브에서 빌드 파일(wheels 포함)을 가져오는 중...")
        try:
            # 기존 빌드 폴더 초기화 후 복원
            subprocess.run(["rm", "-rf", "/content/openvino/build"], check=True)
            os.makedirs("/content/openvino", exist_ok=True)
            subprocess.run(["tar", "-xzf", DRIVE_BUILD_ARCHIVE, "-C", "/content/openvino"], check=True)
            print("✅ [BUILD] 복원 완료!")
        except:
            print("❌ [BUILD] 빌드 폴더 복원 과정에서 에러가 발생했습니다.")
    else:
        print("ℹ️ [BUILD] 저장된 빌드 파일이 없습니다.")
