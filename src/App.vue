<template>
  <v-app id="inspire">
    <!--  navigation-drawer work on desktop res:1080p -->
    <v-navigation-drawer
      v-model="drawer"
      app
      
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>New Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Docker</v-toolbar-title>
      <v-spacer></v-spacer>
        <div class="text-center">
            <v-menu open-on-hover top offset-y>
              <template v-slot:activator="{ on }">
                <v-btn
                  color="primary"
                  dark
                  v-on="on"
                >
                  Dropdown
                </v-btn>
              </template>

              <v-list>
                <v-list-item
                  v-for="(item, index) in items"
                  :key="index"
                  @click=""
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
    </v-app-bar>

    <v-content>
    <router-view></router-view>
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
       items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' },
      ]
    }),
  }
</script>
