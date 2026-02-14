import os
import subprocess

def save(SETTING):
    print("💾 백업 작업을 시작합니다...")
    print(f"📦 [CCACHE] 압축 및 업로드 중...")

    DRIVE_CACHE_ARCHIVE = SETTING["DRIVE_CACHE_ARCHIVE"]
    LOCAL_BIN_DIR = SETTING["LOCAL_BIN_DIR"]
    DRIVE_BIN_ARCHIVE = SETTING["DRIVE_BIN_ARCHIVE"]
    LOCAL_CACHE_DIR = SETTING["LOCAL_CACHE_DIR"]
    DRIVE_BUILD_ARCHIVE = SETTING["DRIVE_BUILD_ARCHIVE"]

    if os.path.exists("/" + LOCAL_CACHE_DIR) and os.listdir("/" + LOCAL_CACHE_DIR):
        try:
            subprocess.run(["tar", "-czf", DRIVE_CACHE_ARCHIVE, "-C", "/", LOCAL_CACHE_DIR], check=True)
            print("✅ [CCACHE] 저장 완료")
            subprocess.run(["ls", "-lh", DRIVE_CACHE_ARCHIVE]) # 용량 확인용
        except subprocess.CalledProcessError:
            print("❌ [CCACHE] tar 압축 과정에서 에러가 발생했습니다.")
    else:
        print("⚠️ [CCACHE] 로컬 캐시 폴더가 비어있거나 존재하지 않습니다. (빌드 시 캐시가 적중되지 않았을 수 있습니다.) 백업을 건너뜁니다.")

    if os.path.exists("/" + LOCAL_BIN_DIR):
        print(f"📦 [BIN] 실행 파일 압축 및 업로드 중...")
        if os.path.exists(DRIVE_BIN_ARCHIVE):
            subprocess.run(["tar", "-czf", DRIVE_BIN_ARCHIVE, "-C", "/content/openvino", "bin"], check=True)
            print("✅ [BIN] 저장 완료")
            subprocess.run(["ls", "-lh", DRIVE_BIN_ARCHIVE], check=True)
        else:
            print("❌ [BIN] 저장 실패")
    else:
        print("⚠️ [BIN] 저장할 bin 폴더가 존재하지 않습니다. 빌드가 실패했나요?")

    print(f"📦 [BUILD] 빌드 파일(wheels 포함) 압축 및 업로드 중...")
    if os.path.exists("/content/openvino/build"):
        try:
            subprocess.run(["tar", "-czf", DRIVE_BUILD_ARCHIVE, "-C", "/content/openvino", "build"], check=True)
            print("✅ [BUILD] 저장 완료")
            subprocess.run(["ls", "-lh", DRIVE_BUILD_ARCHIVE], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ [BUILD] 저장 실패: {e}")
    else:
        print("⚠️ [BUILD] 저장할 build 폴더가 존재하지 않습니다.")

    print("\n🎉 모든 백업 작업이 완료되었습니다.")
    print("\n🎉 모든 백업 작업이 완료되었습니다.")
