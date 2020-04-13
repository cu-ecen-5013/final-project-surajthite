
##############################################################
#
# AESD-ASSIGNMENTS
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
AESD_ASSIGNMENTS_VERSION = bda315f3044bded29d7e3515eb0291f3d116a8b5
AESD_ASSIGNMENTS_SITE = git@github.com:cu-ecen-5013/s20-remote-health-monitoring.git
AESD_ASSIGNMENTS_SITE_METHOD = git


define AESD_ASSIGNMENTS_BUILD_CMDS
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D) all 
endef

#TODO: Add required executables or scripts below
define AESD_ASSIGNMENTS_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 $(@D)/tmp102/tmp102 $(TARGET_DIR)/usr/bin
endef


$(eval $(generic-package))
