<script>
  import { onMount } from "svelte";
  import apiCall from "utils/api-call.js";
  import apiCallDelete from "utils/api-call-delete.js";

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
      const { data, isSuccess } = await apiCallDelete("tournament/" + tournament.code);
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
