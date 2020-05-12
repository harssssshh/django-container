<template>
  <v-img src="https://files02.tchspt.com/articles/wallpapers3/geometric/1.jpg">

  <v-slide-y-transition>

    <v-container>






      <v-layout class="ma-12" row wrap justify-center>
        <v-flex xs10 sm7 md4>
          <v-hover v-slot:default="{hover}" open-delay="50">
            <v-card
              v-show="show11"
              dark
              class="text-xs-center px-3 pa-1 pt-2 mx-3"
              color="rgb(0,0,0,0.3)"
              :elevation="hover?24:4"
            >

              <v-responsive></v-responsive>
              <v-layout id="all" justify-center class="mb-3">
                <v-form>
                  <div>
                    <h1>SIGN UP</h1>
                  </div>
                </v-form>
              </v-layout>
              <v-form ref="Signupform">
                <v-text-field
                  :rules="InputRulesSignupOther"
                  outlined
                  shaped
                  color="orange"
                  label="Username"
                  :type="'text'"
                  prepend-icon="perm_identity"
                ></v-text-field>
                <v-text-field
                  :rules="InputRulesSignupOther"
                  outlined
                  shaped
                  color="orange"
                  label="Email Id"
                  :type="'email'"
                  prepend-icon="mail_outline"
                ></v-text-field>

                <v-text-field
                  :rules="InputRulesSignupPasswword"
                  outlined
                  shaped
                  v-model="passwordsignup"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show1 ? 'text' : 'password'"
                  name="input-10-1"
                  label="Password"
                  color="orange"
                  hint="At least 8 characters"
                  prepend-icon="lock"
                  @click:append="show1 = !show1"
                ></v-text-field>
                <v-text-field
                  :rules="InputRulesSignupPasswword"
                  outlined
                  shaped
                  :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                  prepend-icon="lock"
                  color="orange"
                  counter
                  :type="show2 ? 'text' : 'password'"
                  name="input-10-2"
                  label="Confirm Password"
                  hint="At least 8 characters"
                  class="input-group--focused"
                  @click:append="show2 = !show2"
                ></v-text-field>
              </v-form>

              <v-layout class="mx-9 mb-8">
                <v-flex xs-12 md-2>
                  <v-div>
                    <v-btn @click="submitSignup" elevation="15" color="grey lighten-5 red--text">
                      <span small>Submit</span>
                    </v-btn>
                  </v-div>
                </v-flex>
              </v-layout>
            </v-card>
          </v-hover>
        </v-flex>

        <!-- <v-flex xs10 sm8 md2>

        </v-flex>-->
        <!-- Second flex start -->
        <v-flex xs10 sm7 md4>
          <v-hover v-slot:default="{hover}" open-delay="50">
            <v-card
              v-show="show11"
              dark
              class="text-xs-center red--text pa-4 mt-12"
              :elevation="hover?24:4"
              color="rgb(0,0,0,0.4)"
            >
              <v-responsive></v-responsive>
              <v-layout id="all" justify-center class="mt-7">
                <v-form>
                  <div>
                    <h1>OR</h1>
                  </div>
                </v-form>
              </v-layout>
              <v-layout id="all" justify-center class="mb-5">
                <v-form>
                  <div>
                    <h4>Sign Up with</h4>
                  </div>
                </v-form>
              </v-layout>

              <v-layout justify-center>
                <v-flex xs5 sm5 md3 class="mr-1 ml-2 pl-2">
                  <v-tooltip dark color="red accent-4" top>
                    <template v-slot:activator="{on}">
                      <v-btn fab v-on="on" color="red accent-4">
                        <v-icon color="white">mdi-google</v-icon>
                      </v-btn>
                    </template>
                    <span>Google</span>
                  </v-tooltip>
                </v-flex>
                <v-flex xs4 sm5 md3 class="mx-1 pl-1 pr-1">
                  <v-tooltip bottom dark color="indigo darken-3">
                    <template v-slot:activator="{on}">
                      <v-btn v-on="on" fab color="indigo darken-3">
                        <v-icon x-large color="white">mdi-facebook</v-icon>
                      </v-btn>
                    </template>
                    <span>Facebook</span>
                  </v-tooltip>
                </v-flex>

                <v-flex xs4 sm5 md3 class="mx-1 pr-1">
                  <v-tooltip bottom dark color="blue lighten-1">
                    <template v-slot:activator="{on}">
                      <v-btn fab v-on="on" color="blue lighten-1">
                        <v-icon color="white">mdi-twitter</v-icon>
                      </v-btn>
                    </template>
                    <span>Twitter</span>
                  </v-tooltip>
                </v-flex>

                <v-flex xs4 md3 class="pr-3">
                  <v-tooltip top dark color="blue darken-3">
                    <template v-slot:activator="{on}">
                      <v-btn v-on="on" fab color="white">
                        <v-icon x-large color="blue darken-3">mdi-linkedin</v-icon>
                      </v-btn>
                    </template>
                    <span>LinkedIn</span>
                  </v-tooltip>
                </v-flex>
              </v-layout>

              <v-layout id="all" justify-center class="ma-6">
                <v-form>
                  <div>
                    <h2>ELSE</h2>
                  </div>
                </v-form>
              </v-layout>

              <v-layout justify-center class="ma-6">
                <v-flex xs8 sm8 md8>
                  <v-div>
                    <v-btn
                      outlined
                      rounded
                      large
                      block
                      color="white"
                      @click="show22=true,show11=false"
                    >
                      <span large>LOG IN</span>
                    </v-btn>
                  </v-div>
                </v-flex>
              </v-layout>
            </v-card>
          </v-hover>
        </v-flex>
      </v-layout>

      <!--Second layout fir testing hrere-->

      <v-layout class="ma-3" row wrap justify-center>
        <v-flex xs10 sm7 md4>
          <v-hover v-slot:default="{hover}" open-delay="50">
            <v-card
              v-show="show22"
              dark
              class="text-xs-center pa-6 mt-5 mx-3"
              color="rgb(0,0,0,0.3)"
              :elevation="hover?24:4"
            >
              <v-responsive></v-responsive>
              <v-layout id="all" justify-center class="mb-3">
                <v-form>
                  <div>
                    <h1>LOG IN</h1>
                  </div>
                </v-form>
              </v-layout>
              <v-form ref="Loginform">
                <v-text-field
                  :rules="InputRulesLoginOther"
                  outlined
                  shaped
                  color="orange"
                  label="Username"
                  :type="'text'"
                  prepend-icon="perm_identity"
                ></v-text-field>
                <v-text-field
                  :rules="InputRulesLoginOther"
                  outlined
                  shaped
                  color="orange"
                  label="Email"
                  :type="'email'"
                  prepend-icon="mail_outline"
                ></v-text-field>

                <v-text-field
                  :rules="InputRulesLoginPasswword"
                  outlined
                  shaped
                  v-model="passwordlogin"
                  :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show3 ? 't+ext' : 'password'"
                  name="input-10-1"
                  label="Password"
                  color="orange"
                  hint="At least 8 characters"
                  prepend-icon="lock"
                  @click:append="show3 = !show3"
                ></v-text-field>
              </v-form>

              <v-layout class="mx-9 pb-4">
                <v-flex xs-12 md-2>
                  <v-div>
                    <v-btn @click="submitLogin" elevation="15" color="grey lighten-5 red--text">
                      <span small>Submit</span>
                    </v-btn>
                  </v-div>
                </v-flex>
              </v-layout>
            </v-card>
          </v-hover>
        </v-flex>

        <!-- ljflsdfliflsfsmlfsm -->
        <!-- Second flex start -->
        <v-flex xs10 sm7 md4>
          <v-hover v-slot:default="{hover}" open-delay="50">
            <v-card
              v-show="show22"
              dark
              class="text-xs-center red--text pa-3 mt-12"
              :elevation="hover?24:4"
              color="rgb(0,0,0,0.4)"
            >
              <v-responsive></v-responsive>
              <v-layout id="all" justify-center class="mt-6">
                <v-form>
                  <div>
                    <h1>OR</h1>
                  </div>
                </v-form>
              </v-layout>
              <v-layout id="all" justify-center class="mb-5">
                <v-form>
                  <div>
                    <h4>Log in with</h4>
                  </div>
                </v-form>
              </v-layout>

              <v-layout justify-center>
                <v-flex xs5 sm5 md3 class="mr-1 ml-2 pl-2">
                  <v-tooltip dark color="red accent-4" top>
                    <template v-slot:activator="{on}">
                      <v-btn fab v-on="on" color="red accent-4">
                        <v-icon color="white">mdi-google</v-icon>
                      </v-btn>
                    </template>
                    <span>Google</span>
                  </v-tooltip>
                </v-flex>
                <v-flex xs4 sm5 md3 class="mx-1 pl-1 pr-1">
                  <v-tooltip bottom dark color="indigo darken-3">
                    <template v-slot:activator="{on}">
                      <v-btn v-on="on" fab color="indigo darken-3">
                        <v-icon x-large color="white">mdi-facebook</v-icon>
                      </v-btn>
                    </template>
                    <span>Facebook</span>
                  </v-tooltip>
                </v-flex>

                <v-flex xs4 sm5 md3 class="mx-1 pr-1">
                  <v-tooltip bottom dark color="blue lighten-1">
                    <template v-slot:activator="{on}">
                      <v-btn fab v-on="on" color="blue lighten-1">
                        <v-icon color="white">mdi-twitter</v-icon>
                      </v-btn>
                    </template>
                    <span>Twitter</span>
                  </v-tooltip>
                </v-flex>

                <v-flex xs4 md3 class="ml-1 pr-5">
                  <v-tooltip top dark color="blue darken-3">
                    <template v-slot:activator="{on}">
                      <v-btn v-on="on" fab color="white">
                        <v-icon x-large color="blue darken-3">mdi-linkedin</v-icon>
                      </v-btn>
                    </template>
                    <span>LinkedIn</span>
                  </v-tooltip>
                </v-flex>
              </v-layout>

              <v-layout id="all" justify-center class="ma-6">
                <v-form>
                  <div>
                    <h2>ELSE</h2>
                  </div>
                </v-form>
              </v-layout>

              <v-layout justify-center class="ma-6 mb-8">
                <v-flex xs8 sm8 md8>
                  <v-div>
                    <v-btn
                      outlined
                      rounded
                      large
                      block
                      color="white"
                      @click="show11=true,show22=false"
                    >
                      <span large>SIGN UP</span>
                    </v-btn>
                  </v-div>
                </v-flex>
              </v-layout>
            </v-card>
          </v-hover>
        </v-flex>
      </v-layout>

    </v-container>
  </v-slide-y-transition>
  </v-img>
</template>

<script>
export default {
  data() {
    return {
      passwordlogin: "",
      passwordsignup: "",
      show11: false,
      show22: true,
      show1: "",
      show2: "",
      show3: "",
      show4: "",
      InputRulesLoginPasswword: [
        v => v.length >= 8 || "At least 8 characters required"
      ],
      InputRulesLoginOther: [v => v.length >= 1 || "Cannot submit empty field"],
      InputRulesSignupPasswword: [
        v => v.length >= 8 || "At least 8 characters required"
      ],
      InputRulesSignupOther: [v => v.length >= 1 || "Cannot submit empty field"]
    };
  },
  methods: {
    submitLogin() {
      if (this.$refs.Loginform.validate()) {
        //Code here for log in
        console.log("Log in");
      }
    },
    submitSignup() {
      if (this.$refs.Signupform.validate()) {
        console.log("sign up");
        //Code here for sign up
      }
    }
  }
};
</script>


<style>
#all {
  color: white;
}
</style>
