<template>
  <v-app id="inspire">
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>Signup to proceed</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :href="source"
                      icon
                      large
                      target="_blank"
                      v-on="on"
                    >
                      <v-icon>mdi-code-tags</v-icon>
                    </v-btn>
                  </template>
                  <span>Source</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Username"
                    name="name"
                    prepend-icon="person"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    label="Email"
                    name="emailid"
                    prepend-icon="email"
                    type="email"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    label="Retype Password"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary">Signup</v-btn>
                <div>

              <a class="fb-ic mr-3" role="button"><mdb-icon fab icon="facebook-f" size="lg" /></a>
            </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

    </v-content>
  </v-app>

</template>

<script>
  export default {
    props: {
      source: String,
    },
  }
</script>
