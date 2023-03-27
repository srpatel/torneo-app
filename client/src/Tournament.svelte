<script>
  import { onMount } from "svelte";
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

  async function handleDelete() {
    deleting = true;
    deleting = false;
  }
</script>


<p>Code: {params?.code}</p>
{#if tournament}
  <p>Name: {tournament.name}</p>
  <Space h={2} />
  <div class="form-control w-full max-w-xs">
    <button class="btn" on:click={handleCreate} disabled={deleting}>Delete Tournament</button>
  </div>
{/if}
