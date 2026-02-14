import os
import subprocess

def load(SETTING):
    DRIVE_CACHE_ARCHIVE = SETTING["DRIVE_CACHE_ARCHIVE"]
    DRIVE_BIN_ARCHIVE = SETTING["DRIVE_BIN_ARCHIVE"]
    
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

    # 4. 설정 확인
    print("\n📊 현재 CCACHE 상태:")
    try:
        subprocess.run(["ccache", "-s"], check=True)
    except:
        print("❌ [오류] ccache가 설치되어 있지 않거나 경로를 찾을 수 없습니다. (!apt-get install ccache를 확인하세요)")
