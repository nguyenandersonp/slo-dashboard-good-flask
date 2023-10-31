from _keenthemes.settings import settings
from pprint import pprint
from _keenthemes.libs.theme import KTTheme

"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in _keenthemes/__init__.py
"""
class KTBootstrapDefault:

    def init(context):
        # Init default layout

        """
        See also file starterkit/_keenthemes/__init__.py
        Below layout function need to included with the particular HTML layout file.
        """
        # 1) Light sidebar layout (default.html)
        KTBootstrapDefault.initLightSidebarLayout(context)

        # 2) Dark sidebar layout (default.html)
        # KTBootstrapDefault.initDarkSidebarLayout(context)

        # 3) Dark header layout (default_header_layout.html)
        # KTBootstrapDefault.initDarkHeaderLayout(context)

        # 4) Light header layout (default_header_layout.html)
        # KTBootstrapDefault.initLightHeaderLayout(context)

        # 5) Mini sidebar layout (default_mini_sidebar_layout.html)
        # KTBootstrapDefault.initMiniSidebarLayout(context)

        # 6) Overlay header layout (default_overlay_layout.html)
        # KTBootstrapDefault.initOverlayLayout(context)

        # Init global assets for default layout
        KTBootstrapDefault.initAssets(context)

        return context

    def initAssets(context):
        # Include global vendors
        KTTheme.addVendors(['datatables', 'fullcalendar', 'vis-timeline'])

        # Include global javascript files
        KTTheme.addJavascriptFile('js/widgets.bundle.js')
        KTTheme.addJavascriptFile('js/custom/apps/chat/chat.js')

        KTTheme.addJavascriptFile('js/custom/utilities/modals/upgrade-plan.js')
        KTTheme.addJavascriptFile('js/custom/utilities/modals/create-app.js')
        KTTheme.addJavascriptFile('js/custom/utilities/modals/create-campaign.js')
        KTTheme.addJavascriptFile('js/custom/utilities/modals/users-search.js')
        KTTheme.addJavascriptFile('js/custom/utilities/modals/new-target.js')

        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/main.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/type.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/settings.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/budget.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/team.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/targets.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/files.js")
        KTTheme.addJavascriptFile("js/custom/utilities/modals/create-project/complete.js")

        return context

    def initDarkSidebarLayout(context):
        KTTheme.addHtmlAttribute('body', 'data-kt-app-layout', 'dark-sidebar')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-fixed', 'false')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-fixed', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-hoverable', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-header', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-toolbar', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-footer', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-toolbar-enabled', 'true')

        KTTheme.addHtmlClass('body', 'app-default')

        return context

    def initLightSidebarLayout(context):
        KTTheme.addHtmlAttribute('body', 'data-kt-app-layout', 'light-sidebar')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-fixed', 'false')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-fixed', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-hoverable', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-header', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-toolbar', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-footer', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-toolbar-enabled', 'true')

        KTTheme.addHtmlClass('body', 'app-default')

        return context

    def initDarkHeaderLayout(context):
        KTTheme.addHtmlAttribute('body', 'data-kt-app-layout', 'dark-header')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-toolbar-enabled', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-stacked', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-primary-enabled', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-secondary-enabled', 'true')

        KTTheme.addHtmlClass('body', 'app-default')

        return context

    def initLightHeaderLayout(context):
        KTTheme.addHtmlAttribute('body', 'data-kt-app-layout', 'light-header')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-toolbar-enabled', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-stacked', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-primary-enabled', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-header-secondary-enabled', 'true')

        KTTheme.addHtmlClass('body', 'app-default')

        return context

    def initMiniSidebarLayout(context):
        KTTheme.addHtmlAttribute('body', 'data-kt-app-layout', 'mini-sidebar')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-enabled', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-fixed', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-header', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-toolbar', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-footer', 'true')

        KTTheme.addHtmlClass('body', 'app-default')

        return context

    def initOverlayLayout(context):
        KTTheme.addHtmlAttribute('body', 'data-kt-app-layout', 'overlay')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-enabled', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-fixed', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-header', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-toolbar', 'true')
        KTTheme.addHtmlAttribute('body', 'data-kt-app-sidebar-push-footer', 'true')

        KTTheme.addHtmlClass('body', 'app-default')

        return context