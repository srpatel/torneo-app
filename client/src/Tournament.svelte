<script>
  import { onMount } from "svelte";
  import { push } from "svelte-spa-router";
  import apiCall from "utils/api-call.js";

  export let params;

  let tournament = null;

  onMount(async () => {
    // Load tournament list from db
    if (params?.code) {
        const response = await apiCall("tournament/" + params.code);
        if (response.isSuccess) {
            tournament = response.data;
        }
    }
  });

  let deleting = false;
  let error = null;

  async function handleDelete() {
    deleting = true;
    try {
      const { data, isSuccess } = await apiCall("tournament/" + tournament.code, null, "DELETE");
      if (isSuccess) {
        push("/");
      } else {
        error = data.detail;
      }
    } catch (e) {
      console.error(e);
    }
    deleting = false;
  }
</script>


<p>Code: {params?.code}</p>
{#if tournament}
  <p>Name: {tournament.name}</p>
  <div class="form-control w-full max-w-xs">
    <button class="btn" on:click={handleDelete} disabled={deleting}>Delete Tournament</button>
  </div>
{/if}
