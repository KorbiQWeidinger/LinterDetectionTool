NAME = "PVS-Studio"

file_regex = {
    "PVS-Studio-Java", "PVS-Studio", ".*pvs.*", ".*pvsstudio.*", ".*pvs-studio.*"                   # name
}

signal_words = {
    "PVS-Studio", "pvs-studio", "pvsstudio", "PVSStudio",                               # name
    "pvs-studio-analyzer", "PVS_STUDIO_CORE", "pvsstudio-cores",                        # https://pvs-studio.com/en/docs/manual/0047/
    "PVS-Studio-Java", "SHORT_VERSION_PVS", "pvsAnalyze",                               # https://pvs-studio.com/en/docs/manual/0047/
    "com.pvsstudio", "pvsstudio-maven-plugin", "com.pvsstudio.PvsStudioGradlePlugin",
}
