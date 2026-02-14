import os

def save(SETTING):
    print("💾 백업 작업을 시작합니다...")
    print(f"📦 [CCACHE] 압축 및 업로드 중...")

    DRIVE_CACHE_ARCHIVE = SETTING["DRIVE_CACHE_ARCHIVE"]
    LOCAL_BIN_DIR = SETTING["LOCAL_BIN_DIR"]
    DRIVE_BIN_ARCHIVE = SETTING["DRIVE_BIN_ARCHIVE"]

    os.system(f"tar -czf '{DRIVE_CACHE_ARCHIVE}' -C / content/ccache_local")
    if os.path.exists(DRIVE_CACHE_ARCHIVE):
        print("✅ [CCACHE] 저장 완료")
    else:
        print("❌ [CCACHE] 저장 실패")

    if os.path.exists("/" + LOCAL_BIN_DIR):
        print(f"📦 [BIN] 실행 파일 압축 및 업로드 중...")
        os.system(f"tar -czf '{DRIVE_BIN_ARCHIVE}' -C / content/ccache_local")
        if os.path.exists(DRIVE_BIN_ARCHIVE):
            print("✅ [BIN] 저장 완료")
            os.system(f"ls -lh '{DRIVE_BIN_ARCHIVE}'")
        else:
            print("❌ [BIN] 저장 실패")
    else:
        print("⚠️ [BIN] 저장할 bin 폴더가 존재하지 않습니다. 빌드가 실패했나요?")
    print("\n🎉 모든 백업 작업이 완료되었습니다.")
