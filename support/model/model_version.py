from support.model.repository.model_version_repository import ModelVersionRepository


class ModelVersion:
    def __init__(self,
                 model_name: str,
                 model_version_repository=ModelVersionRepository()):
        self._model_name = model_name
        self._model_version_repository = model_version_repository

    def get_model_version(self):
        return self._model_version_repository.get_current_model_version(model_name=self._model_name)

    def get_ct_model_version(self):
        """ 지속적학습(CT) 모델 버전을 조회 한다. """

        # 현재 모델 버전을 조회 한다.
        current_model_version = self.get_model_version()
        if current_model_version is None:  # 모델 버전 미존재 시
            return "1.0.0"

        # 모델 버전을 major, miner, patch 으로 분리 한다.
        model_version = current_model_version.split(".")
        major = model_version[0]
        miner = model_version[1]
        patch = int(model_version[2])

        # patch 버전을 1 증가 시킨다.
        patch += 1

        # CT 모델버전을 조립 한다.
        ct_model_version = ".".join([major, miner, str(patch)])
        return ct_model_version
